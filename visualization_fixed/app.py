from flask import Flask, flash, redirect, render_template, request, session, abort
# from bokeh.embed import server_document
import pandas as pd

from bokeh.layouts import row, column
from bokeh.models import Select
from bokeh.palettes import Spectral5
from bokeh.plotting import curdoc, figure
from bokeh.embed import components
from bokeh.themes import Theme
from bokeh.sampledata.autompg import autompg_clean as df
from flask import Flask, render_template
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

app = Flask(__name__)

@app.route("/")
def hello():

    df = pd.read_csv('./TABLE_LOS.csv')

    df2 = pd.read_csv('./people.csv')

    SIZES = list(range(6, 22, 3))
    COLORS = Spectral5
    N_SIZES = len(SIZES)
    N_COLORS = len(COLORS)

    # data cleanup
    df.INSURANCE = df.INSURANCE.astype(str)
    df.RACE = df.RACE.astype(str)
    df.LANGUAGE = df.LANGUAGE.astype(str)
    df.MARITAL = df.MARITAL.astype(str)

    df2.INSURANCE = df2.INSURANCE.astype(str)
    df2.RACE = df2.RACE.astype(str)
    df2.LANGUAGE = df2.LANGUAGE.astype(str)
    df2.MARITAL = df2.MARITAL.astype(str)

    df['xPredict_INSURANCE'] = df2['INSURANCE']
    df['xPredict_RACE'] = df2['RACE']
    df['xPredict_LANGUAGE'] = df2['LANGUAGE']
    df['xPredict_MARITAL'] = df2['MARITAL']
    df['xPredict_LOS'] = df2['LOS']

    del df['PATIENT_ID']

    columns = sorted(df.columns)
    discrete = [x for x in columns if df[x].dtype == object]
    continuous = [x for x in columns if x not in discrete]


    def create_figure():
        xs = df[x.value].values
        ys = df[y.value].values
        x_title = x.value.title()
        y_title = y.value.title()

        kw = dict()
        if x.value in discrete:
            kw['x_range'] = sorted(set(xs))
        if y.value in discrete:
            kw['y_range'] = sorted(set(ys))
        kw['title'] = "%s vs %s" % (x_title, y_title)

        p = figure(plot_height=600, plot_width=800, tools='pan,box_zoom,hover,reset', **kw)
        p.xaxis.axis_label = x_title
        p.yaxis.axis_label = y_title

        if x.value in discrete:
            p.xaxis.major_label_orientation = pd.np.pi / 4

        sz = 9
        if size.value != 'None':
            if len(set(df[size.value])) > N_SIZES:
                groups = pd.qcut(df[size.value].values, N_SIZES, duplicates='drop')
            else:
                groups = pd.Categorical(df[size.value])
            sz = [SIZES[xx] for xx in groups.codes]

        c = "#680000"
        if color.value != 'None':
            if len(set(df[color.value])) > N_SIZES:
                groups = pd.qcut(df[color.value].values, N_COLORS, duplicates='drop')
            else:
                groups = pd.Categorical(df[color.value])
            c = [COLORS[xx] for xx in groups.codes]

        p.circle(x=xs, y=ys, color=c, size=sz, line_color="black", alpha=0.6, hover_color='black', hover_alpha=0.5)

        return p


    def update(attr, old, new):
        layout.children[1] = create_figure()

    x = Select(title='X-Axis', value='INSURANCE', options=columns)
    x.on_change('value', update)

    y = Select(title='Y-Axis', value='RACE', options=columns)
    y.on_change('value', update)

    size = Select(title='Size', value='None', options=['None'] + continuous)
    size.on_change('value', update)

    color = Select(title='Color', value='None', options=['None'] + continuous)
    color.on_change('value', update)

    controls = column([x, y, color, size], width=200)
    layout = row(controls, create_figure())

    curdoc().add_root(layout)
    curdoc().title = "LOS_Visualizer"

    curdoc().theme = Theme(filename="./theme.yaml")
    
    # layout1 = layout.children[1]

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(layout)
    return render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    # return encode_utf8(html)

    # script, div = components(layout1)

    # # return render_template('index.html')
    # return render_template("index.html",
                           # div=div, script=script)

if __name__ == "__main__":
    app.run()
