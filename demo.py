
import streamlit as st

import numpy as np
import pandas as pd

'# Inline documentation'

'Any streamlit method called without parenthesis and arguments will display its documentation'

with st.echo():
    st.echo

'# Magic commands'

with st.echo():
    'some text or **markdown**'

'# Text'

with st.echo():
    st.text('hello')

'# Markdown'

'Markdown allows to structure your app into sections'

with st.echo():
    st.markdown("""
    # title

    ## many levels of subtitles

    **bold** or *italic* text with [links](http://github.com/streamlit) and:
    - bullet points
    """)

'# Latex'

with st.echo():
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
        ''')

'# Functions'

with st.echo():
    def fun(a, b):
        '''docstring of the function'''
        return a + b

    st.write(fun)

'# Objects'

with st.echo():
    dictionary = { 'a' : 1, 'b' : 2 }

    st.write(dictionary)

'# Json'

with st.echo():
    seb = '''
        {
          "login": "ssaunier",
          "id": 414418,
          "node_id": "MDQ6VXNlcjQxNDQxOA==",
          "avatar_url": "https://avatars3.githubusercontent.com/u/414418?v=4",
          "created_at": "2010-09-24T13:31:21Z",
          "updated_at": "2020-08-08T14:26:53Z"
        }
    '''
    st.json(seb)

'# Echo'

'Display blocks of executed code'

with st.echo():
    with st.echo():
        st.write('hey')

'# Code'

with st.echo():
    st.code('''
    def function sum(a, b):
        return a + b
    ''')

'# DataFrame'

with st.echo():
    df = pd.DataFrame({
      'first column': list(range(1, 11)),
      'second column': np.arange(10, 101, 10)
    })

    st.table(df.head())

    df

'## Using Pandas Styler'

with st.echo():
    dataframe = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)))

    st.dataframe(dataframe.style.highlight_max(axis=0))

'# Check box'

with st.echo():
    if st.checkbox('Show content'):
        'Any set of text or widgets'

'# Radio'

with st.echo():
    direction = st.radio('Select a direction', ('top', 'right', 'bottom', 'left'))
    direction

# '# Spinner'

# if st.checkbox('Show spinner'):
#     import time

#     with st.echo():
#         with st.spinner('Wait for it...'):
#             time.sleep(5)
#         st.success('Done!')

'# Progress bar'

if st.checkbox('Show progress bar'):
    import time

    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.1)

    '...and now we\'re done!'

'# button'

with st.echo():
    if st.button('click me'):
        # print is visible in server output, not in the page
        print('button clicked!')
        'I was clicked 🎉'
    else:
        'I was not clicked 😞'

'# Select box, multi select'

with st.echo():
    option = st.selectbox('Select a line to filter', df['first column'])

    df[df['first column'] == option]

'# Slider'

with st.echo():
    option = st.slider('Select a modulus', 1, 10, 3)

    df[df['first column'] % option == 0]

'# Text input'

with st.echo():
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

'# Text area'

with st.echo():
    txt = st.text_area('Text to analyze', '''
        It was the best of times, it was the worst of times, it was
        the age of wisdom, it was the age of foolishness, (...)
        ''')
    st.write('Length:', len(txt))

'# Number input'

with st.echo():
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)

'# Date input'

with st.echo():
    import datetime
    d = st.date_input(
        "When's your birthday",
        datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)

'# Time input'

with st.echo():
    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for', t)

'# File uploader'

with st.echo():
    st.set_option('deprecation.showfileUploaderEncoding', False)
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

'# Error, warning, info, success'

with st.echo():
    st.success('This is a success message!')

'# Line chart'

with st.echo():
    df = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

    st.line_chart(df)

'# Area chart'

with st.echo():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.area_chart(chart_data)


'# Bar chart'

with st.echo():
    df = pd.DataFrame(
            np.random.randn(200, 1),
            columns=['a'])

    hist_values = np.histogram(
        df.a, bins=25)[0]

    st.bar_chart(hist_values)

with st.echo():
    chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["a", "b", "c"])

    st.bar_chart(chart_data)

'# Map'

with st.echo():
    map_df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_df)

'# Cache'

with st.echo():
    df = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

    df

st.slider('Show me uncached changes', 1, 10, 1)

with st.echo():
    @st.cache
    def get_data():
        return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c'])

    cached_df = get_data()

    cached_df

option = st.slider('Zoom', 1, 10, 1)

'### Uncached random df'

st.line_chart(df)

'### Cached random df'

st.line_chart(cached_df)

'### Impact of slider on cached df'

new = cached_df.copy(True)
new['a'] = cached_df['a'] / option

st.line_chart(new)

'# Sidebar'

with st.echo():
    st.sidebar.markdown(f"""
        # Title
        Selected option: {option}
        """)

'# Styling your pages with CSS 🤩'

with st.echo():
    CSS = """
    h1 {
        color: red;
    }
    body {
        background-image: url(https://avatars1.githubusercontent.com/u/9978111?v=4);
        background-size: cover;
    }
    """

    if st.checkbox('Inject CSS'):
        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'# Using sections'

SECTION_CSS = """
.wagon-container {
    display: flex;
}

.left, .right {
    width: 500px;
    height: 500px;
}

.left {
    background-color: red;
}

.right {
    background-color: green;
}
"""

SECTION_HTML = """
<div class="wagon-container">
    <div class="left">
    </div>
    <div class="right">
    </div>
</div>
"""

INJECTED_HTML = f"""
<style>
{SECTION_CSS}
</style>
{SECTION_HTML}
"""

st.write(INJECTED_HTML, unsafe_allow_html=True)

'# Using sections'

if st.checkbox('Show teachers'):
    image_size = st.slider('Zoom', 50, 250, 119)

    # https://kitt.lewagon.com/camps/414/contracts
    # document.querySelectorAll('tr').forEach(elt => {
    #     const img = elt.getElementsByTagName('img');
    #     if (img.length > 0) {
    #         const name = elt.getElementsByTagName('td')[1].innerText;
    #         const src = img[0].src;
    #         console.log(`'${name}' : '${src}',`);
    #     }
    # });

    TEACHERS = {
        'Bruno Lajoie' : 'https://avatars1.githubusercontent.com/u/22095643?v=4',
        'Kevin Robert' : 'https://avatars1.githubusercontent.com/u/9978111?v=4',
        'Julien Pelegri' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1563814498/fku9zvwyhuqkcpwoixls.jpg',
        'Sébastien Saunier' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1558950804/lxpghuy9ljoa9mcwrrby.jpg',
        'Damien Milon' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1532100716/quohyte0kozuvxlwgn0s.jpg',
        'Benjamin Baranger' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1536827206/ixr9unj1pvqtkfbzvlcu.jpg',
        'Lucien George' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1581954281/yufygsunlebymjwtxqpi.jpg',
        'Zuza Żuber' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570609465/a8kmugjdqlihecdk9cz8.jpg',
        'Benjamin Auzanneau' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570874395/gykb7mofng5jiumfhxih.jpg',
        'Igor Koval' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570875813/iwzfmio7d8n4qghlx00w.jpg',
        'Jean Bizot' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570875224/ocypfncdlmcpxd1v60zp.jpg',
        'Hadrien Jean' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570874079/b0jtipxjdruewdjiwjrh.jpg',
        'Davy Wai' : 'https://avatars3.githubusercontent.com/u/42499767?v=4',
        'Gaëtan Manchon' : 'https://avatars1.githubusercontent.com/u/34584935?v=4',
        'Matthieu Rousseau' : 'https://avatars0.githubusercontent.com/u/16851063?v=4',
        'Aurélien Allard' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1510128505/glgkbr1dc52wihgokplh.jpg',
        'Soumia Ghalim' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1587463683/xqicgayidgkjzkwd2gvn.jpg',
        'Paul Chabbert' : 'https://avatars2.githubusercontent.com/u/47640935?v=4',
        'Loïc Chesneau' : 'https://avatars3.githubusercontent.com/u/21106392?v=4',
        'Eloïse Gomez' : 'https://avatars2.githubusercontent.com/u/52004932?v=4',
        'Thibault Pedelhez' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570454328/ma72namffbsh1vlso3c8.jpg',
        'Hugo Vandernotte' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1516582640/xgp9icrtsu0bzt2jtjrl.jpg',
        'Victor Challier' : 'https://avatars2.githubusercontent.com/u/36234477?v=4',
        'Julien Parenti' : 'https://avatars1.githubusercontent.com/u/22306617?v=4'
    }

    TEACHER_CSS = f"""
    #teachers {{
        display: flex;
        flex-wrap: wrap;
    }}

    .teacher-card {{
        display: flex;
        flex-direction: column;
    }}

    .teacher-card img {{
        width: {image_size}px;
        height: {image_size}px;
        border-radius: 100%;
        padding: 4px;
        margin: 10px;
        box-shadow: 0 0 4px #eee;
    }}

    .teacher-card span {{
        text-align: center;
    }}
    """

    # streamlit html injection seems to sensitive to new lines...
    # remove that \ and the html gets displayed instead of being interpreted
    TEACHER_CARD = """\
        <div class="teacher-card">
            <img src="{url}">
            <span>{name}</span>
        </div>
    """

    teachers = ''.join([TEACHER_CARD.format(name=f'{name.split()[0]}', url=url) for name, url in TEACHERS.items()])

    TEACHER_HTML = f"""
    <style>
    {TEACHER_CSS}
    </style>
    <div id="teachers">
        {teachers}
    </div>
    """

    st.write(TEACHER_HTML, unsafe_allow_html=True)

'# Scrapping Le Wagon Privacy Policy! 🥳'

if st.checkbox('Inject the CSS for the privacy policy 😋'):
    st.write('<link href="https://www.iubenda.com/assets/privacy_policy-4925cabc28812855d7c0a24b1f0c961c.css" media="screen" rel="stylesheet" type="text/css" />', unsafe_allow_html=True)

if st.checkbox('Inject the privacy policy 😋'):
    with st.echo():
        import requests
        from bs4 import BeautifulSoup

        response = requests.get('https://www.iubenda.com/privacy-policy/7967062/legal')

        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.select('#wbars_all')

        st.write(f'<div id="iubenda_policy" class="iubenda_fixed_policy">{str(content)}</div>', unsafe_allow_html=True)

'# Matplotlib'

with st.echo():
    import matplotlib.pyplot as plt

    from scipy import misc
    face = misc.face(gray=True)
    plt.imshow(face, cmap='gray')

    st.pyplot()

'# Plotly'

with st.echo():
    import plotly.graph_objects as go

    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
    st.plotly_chart(fig)

'# Altair, Vega Lite, Bokeh, pydeck, Deck GL, Graphviz'

with st.echo():
    import pandas as pd
    import numpy as np
    import altair as alt

    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

    st.write(c)

'# Images, Audio, Video'

with st.echo():
    from PIL import Image
    image = Image.open('wagon.png')
    st.image(image, caption='Le Wagon', use_column_width=False)

'# Screencast'

'Top right'

'# Magnificent balloons'

with st.echo():
    if st.button('More 🎈🎈🎈 please!'):
        st.balloons()
