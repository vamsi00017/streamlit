import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import io

st.set_page_config(layout="wide", page_title="Streamlit Demo", page_icon="🚀")
st.sidebar.title("Demo Navigation")
demo_section = st.sidebar.radio(
    "Choose a section:",
    [
        "Introduction",
        "Text Elements",
        "Data Display",
        "Charts & Maps",
        "Media Elements",
        "Interactive Widgets",
        "Layout Options",
        "Session State",
        "Caching",
        "Status & Progress",
        "Custom Components",
        "Advanced & Experimental Features" 
    ]
)

@st.cache_data(ttl=3600)
def load_expensive_data():
    """Simulates loading a large dataset."""
    time.sleep(2)
    data = pd.DataFrame(
        np.random.randn(500, 5),
        columns=[f"Col {i+1}" for i in range(5)]
    )
    return data

@st.cache_resource 
def load_expensive_model():
    """Simulates loading a large machine learning model."""
    time.sleep(3) 
    return "Simulated ML Model (Global Resource)"

def increment_counter():
    """Callback function to increment session state counter."""
    st.session_state.counter += 1

def update_text_input():
    """Callback function to update session state text."""
    st.session_state.persisted_text = st.session_state.text_input_widget


st.title("Streamlit Demo: Exploring Functionalities 🚀")
st.markdown("This interactive application showcases a wide range of Streamlit's capabilities, from basic display to advanced features like session state and caching. Use the sidebar to navigate through different sections.")
st.divider()

if demo_section == "Introduction":
    st.header("Welcome to the Streamlit Power Demo!")
    st.write("""
    Streamlit simplifies the creation of interactive web applications using pure Python.
    Its core strength lies in its ability to turn data scripts into shareable web apps
    in minutes, without requiring front-end development expertise.
    """)
    st.info("Interact with the widgets and observe how the application updates in real-time!")
    st.markdown("---")
    st.subheader("The Streamlit Execution Model")
    st.write("""
    A fundamental concept in Streamlit is its execution model: the entire Python script
    reruns from top to bottom whenever a user interacts with a widget or the source code is modified.
    This creates a fast interactive loop, where widgets are treated like variables that update
    with user input.
    """)
    st.code("""
    import streamlit as st
    x = st.slider('x') # This is a widget
    st.write(x, 'squared is', x * x)
    """)
    st.write("On first run, the app above outputs '0 squared is 0'. Interacting with the slider reruns the script, updating 'x'.")
    st.markdown("---")
    st.subheader("Magic Commands and `st.write()`")
    st.write("""
    `st.write()` is Streamlit's versatile "Swiss Army knife" for displaying content.
    It intelligently renders various data types. You can also use "magic commands"
    by simply typing a variable or expression on a line.
    """)
    st.code("""
    import streamlit as st
    st.write("Hello, Streamlit!")
    my_variable = "This is a magic string!"
    my_variable # Magic command
    """)
    st.write("Try typing `st.session_state` on a line in your actual app to see its contents!")

elif demo_section == "Text Elements":
    st.header("1. Text and Markdown Elements")
    st.write("Streamlit offers diverse options for displaying textual content.")
    st.subheader("Main Headings")
    st.markdown("`st.title()`: The highest level heading for your app.")
    st.title("App Title Example")
    st.markdown("`st.header()`: A primary section heading.")
    st.header("Section Header Example")
    st.markdown("`st.subheader()`: A secondary section heading.")
    st.subheader("Subsection Subheader Example")
    st.subheader("Formatted Text")
    st.markdown("`st.markdown()`: Renders text with **Markdown** formatting.")
    st.markdown("This is a **bold** text, *italic* text, and `inline code`.")
    st.markdown("(https://docs.streamlit.io/)")
    st.markdown("`st.text()`: Displays raw, fixed-width text.")
    st.text("This is preformatted text.\nIt respects line breaks.")
    st.markdown("`st.caption()`: Displays text in a smaller font.")
    st.caption("This is a small caption, often used for footnotes or descriptions.")
    st.markdown("`st.code()`: Displays code blocks with syntax highlighting.")
    st.code("""
    import pandas as pd
    import numpy as np
    # Example Python code
    def greet(name):
      return f"Hello, {name}!"
    """, language="python")
    st.markdown("`st.latex()`: Renders mathematical expressions using LaTeX.")
    st.latex(r"""
    E=mc^2 \\
    \int_0^1 x^2 dx = \frac{1}{3}
    """)
    st.markdown("`st.divider()`: Inserts a horizontal rule.")
    st.divider()
    st.write("Content below the divider.")
    st.markdown("`st.badge()`: Displays a small, colored badge.")
    st.info("[New Feature]", icon="✅")
    st.warning("[Beta]", icon="⚠️")
    st.subheader("Echoing Code")
    st.markdown("`st.echo()`: Displays the code block before executing it. Useful for tutorials.")
    with st.echo():
        st.write("This line of code is displayed above.")
        x = 10
        st.write(f"The value of x is {x}.")

elif demo_section == "Data Display":
    st.header("2. Data Display Elements")
    st.write("Streamlit allows displaying tabular data in various interactive and static formats.")
    st.subheader("Interactive DataFrames (`st.dataframe`)")
    st.markdown("`st.dataframe()` displays an interactive table, supporting various data types. It allows sorting, searching, and styling.")
    data_for_df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=[f'Col {i+1}' for i in range(5)]
    )
    st.dataframe(data_for_df)
    st.markdown("#### Styling with Pandas Styler")
    st.write("You can apply custom styling using `pandas.Styler`.")
    styled_df = pd.DataFrame(
        np.random.rand(5, 3),
        columns=[f"A{i+1}" for i in range(3)]
    )
    st.dataframe(styled_df.style.highlight_max(axis=0).background_gradient(cmap='viridis'))
    st.markdown("#### Column Configuration")
    st.write("Customize column display, e.g., hide index, set column order, format numbers.")
    config_df = pd.DataFrame({
        'Sales': [100, 200, 150, 300],
        'Product': ['A', 'B', 'C', 'D'],
        'Date': pd.to_datetime(['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15']),
        'Price': [10.5, 20.0, 5.75, 12.25]
    })
    column_order = ['Product', 'Sales', 'Date', 'Price']
    st.dataframe(
        config_df,
        hide_index=True,
        column_order=column_order,
        column_config={
            "Sales": st.column_config.NumberColumn(
                "Total Sales", format="$%d"
            ),
            "Date": st.column_config.DateColumn(
                "Sale Date", format="YYYY/MM/DD"
            ),
            "Price": st.column_config.NumberColumn(
                "Unit Price", format="$%.2f"
            )
        }
    )
    st.markdown("#### Interactive Selection (`on_select`)")
    st.write("Enable row/column selection to trigger actions.")
    selection_df = pd.DataFrame(
        {"col1": [1, 2, 3], "col2": ["A", "B", "C"], "col3": [True, False, True]}
    )
    selected_rows = st.dataframe(selection_df, on_select="rerun", selection_mode="single-row")
    if selected_rows.selection.rows:
        st.write("Selected rows:", selection_df.iloc[selected_rows.selection.rows])
    st.subheader("Static Tables (`st.table`)")
    st.markdown("`st.table()` displays a static table, useful for small, fixed datasets.")
    static_data = pd.DataFrame({
        'Category': ['Fruit', 'Vegetable', 'Dairy'],
        'Items': ['Apple', 'Carrot', 'Milk']
    })
    st.table(static_data)
    st.subheader("Dynamically Adding Rows (`element.add_rows`)")
    st.write("You can append new rows to existing dataframe elements.")
    initial_df = pd.DataFrame(np.random.rand(3, 2), columns=['X', 'Y'])
    my_dynamic_table = st.dataframe(initial_df)
    if st.button("Add 2 More Rows"):
        new_rows = pd.DataFrame(np.random.rand(2, 2), columns=['X', 'Y'])
        my_dynamic_table.add_rows(new_rows)
        st.success("Rows added!")

elif demo_section == "Charts & Maps":
    st.header("3. Charts and Visualizations")
    st.write("Streamlit integrates with popular charting libraries and offers simplified native charts.")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.subheader("Simple Charts (Native Streamlit)")
    st.markdown("`st.line_chart()`: Displays a line chart.")
    st.line_chart(chart_data)
    st.markdown("`st.bar_chart()`: Displays a bar chart.")
    st.bar_chart(chart_data)
    st.markdown("`st.area_chart()`: Displays an area chart.")
    st.area_chart(chart_data)
    st.markdown("`st.scatter_chart()`: Displays a scatter chart.")
    st.scatter_chart(chart_data, x='a', y='b', color='c')
    st.subheader("Maps (`st.map`)")
    st.markdown("`st.map()`: Plots data points on a map, great for geospatial data.")
    map_data = pd.DataFrame(
        np.random.randn(100, 2) + [37.76, -122.4], # Use + instead of /
        columns=['lat', 'lon']
    )
    st.map(map_data)
    st.subheader("Advanced Chart Integrations (Matplotlib Example)")
    st.markdown("`st.pyplot()`: Displays Matplotlib figures for custom plots.")
    fig, ax = plt.subplots()
    ax.hist(np.random.randn(100), bins=20)
    ax.set_title("Matplotlib Histogram Example")
    st.pyplot(fig)
    st.write("""
    Streamlit also supports `st.altair_chart()`, `st.plotly_chart()`, `st.bokeh_chart()`,
    `st.pydeck_chart()`, `st.vega_lite_chart()`, and `st.graphviz_chart()` for more
    specialized and interactive visualizations.
    """)

elif demo_section == "Media Elements":
    st.header("4. Media Elements")
    st.write("Easily embed images, audio, and video into your Streamlit apps.")
    st.subheader("Images (`st.image`)")
    st.markdown("`st.image()`: Displays static images.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-light.svg",
        caption="Streamlit Logo from URL", width=200)
    try:
        st.image("https://picsum.photos/400/200", caption="Random Image from Picsum", use_column_width=True)
    except Exception:
        st.info("To display a local image, place an image file (e.g., 'local_image.jpg') in the same directory.")
    st.subheader("Audio (`st.audio`)")
    st.markdown("`st.audio()`: Embeds an audio player.")
    audio_bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    st.audio(audio_bytes, format="audio/wav", start_time=0)
    st.info("Replace `audio_bytes` with actual audio data or a URL to play sound.")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3", start_time=10)
    st.subheader("Video (`st.video`)")
    st.markdown("`st.video()`: Embeds a video player, supporting URLs including YouTube.")
    st.video("http://www.youtube.com/watch?v=D0D4Pa22iG0", start_time=60, loop=True)
    st.write("This is a Streamlit tutorial video, starting at 1 minute and looping.")

elif demo_section == "Interactive Widgets":
    st.header("5. Interactive Widgets: Capturing User Input")
    st.write("Streamlit's widgets allow users to interact with the application and provide input.")
    st.subheader("Buttons and Links")
    if st.button("Click Me!"):
        st.success("Button clicked!")
    text_contents = "This is some dummy text for download."
    st.download_button(
        label="Download Dummy Text",
        data=text_contents,
        file_name="dummy_text.txt",
        mime="text/plain"
    )
    st.link_button("Go to Streamlit.io", url="https://streamlit.io")
    st.subheader("Selection Widgets")
    show_content = st.checkbox("Show additional content?")
    if show_content:
        st.info("This content is shown because the checkbox is checked.")
    radio_choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {radio_choice}")
    select_box_choice = st.selectbox("Select from dropdown:", ["Red", "Green", "Blue"])
    st.write(f"Dropdown selected: {select_box_choice}")
    multi_select_choices = st.multiselect("Select multiple colors:", ["Red", "Green", "Blue"])
    st.write(f"You selected: {', '.join(multi_select_choices)}")
    toggle_state = st.toggle("Activate Feature Toggle")
    if toggle_state:
        st.success("Feature is ON!")
    else:
        st.warning("Feature is OFF.")
    color = st.color_picker("Pick a color", '#00f900')
    st.write('The current color is', color)
    st.subheader("Numeric and Date/Time Inputs")
    num_slider = st.slider("Select a number (slider)", 0, 100, 25)
    st.write(f"Slider value: {num_slider}")
    num_input = st.number_input("Enter a number (numeric input)", 0, 100, 50)
    st.write(f"Numeric input value: {num_input}")
    today = st.date_input("Select a date")
    st.write(f"Selected date: {today}")
    now = st.time_input("Select a time")
    st.write(f"Selected time: {now}")
    st.subheader("Text and File Inputs")
    user_name = st.text_input("Enter your name:")
    if user_name:
        st.write(f"Hello, {user_name}!")
    long_text = st.text_area("Enter a multi-line text:")
    if long_text:
        st.write("You entered:")
        st.info(long_text)
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file is not None:
        df_uploaded = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df_uploaded.head())
    st.subheader("Chat Input")
    chat_message = st.chat_input("Say something about Streamlit...")
    if chat_message:
        st.write(f"You said: {chat_message}")
    st.subheader("Data Editor")
    editable_df = pd.DataFrame(
        {"Column A": [1, 2, 3], "Column B": ["X", "Y", "Z"]}
    )
    st.write("Edit the DataFrame directly:")
    edited_data = st.data_editor(editable_df, num_rows="dynamic")
    st.write("Edited data:")
    st.dataframe(edited_data)

elif demo_section == "Layout Options":
    st.header("6. Layout and Structure")
    st.write("Organize your application content effectively using Streamlit's layout options.")
    st.subheader("Columns (`st.columns`)")
    st.markdown("Divide your content into side-by-side columns.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("This is Column 1")
        st.button("Button 1")
    with col2:
        st.info("This is Column 2")
        st.slider("Slider 2", 0, 10)
    with col3:
        st.warning("This is Column 3")
        st.text_input("Input 3")
    st.subheader("Containers (`st.container`)")
    st.markdown("Group related elements together.")
    with st.container(border=True):
        st.write("This content is inside a container.")
        st.checkbox("Container checkbox")
    st.subheader("Expanders (`st.expander`)")
    st.markdown("Hide and reveal content to save space.")
    with st.expander("Click to see more details"):
        st.write("This is hidden content that appears when the expander is open.")
        st.image("https://picsum.photos/200/100", caption="Image inside expander")
    st.subheader("Tabs (`st.tabs`)")
    st.markdown("Organize content into distinct, navigable tabs.")
    tab1, tab2 = st.tabs(["Data View", "Chart View"])
    with tab1:
        st.write("This is the Data View tab.")
        st.dataframe(pd.DataFrame({'col': [1, 2, 3]}))
    with tab2:
        st.write("This is the Chart View tab.")
        st.line_chart(pd.DataFrame(np.random.randn(10,1), columns=['value']))
    st.subheader("Sidebar (`st.sidebar`)")
    st.markdown("Elements placed in `st.sidebar` appear on the left sidebar.")
    st.sidebar.write("---")
    st.sidebar.subheader("Sidebar Content")
    st.sidebar.text_input("Sidebar Input")
    st.sidebar.button("Sidebar Button")
    st.subheader("Forms (`st.form`)")
    st.markdown("Group input widgets and submit them atomically.")
    with st.form(key="my_form"):
        st.write("Inside the form")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0)
        submitted = st.form_submit_button("Submit Form")
        if submitted:
            st.success(f"Form Submitted! Name: {name}, Age: {age}")

elif demo_section == "Session State":
    st.header("7. Session State: Persisting User Interactions")
    st.write("Session State allows you to maintain data across script reruns for a single user session.")
    st.subheader("Basic Session State Usage")
    st.markdown("Initialize and update a counter that persists across interactions.")
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    st.write(f"Current counter value: {st.session_state.counter}")
    st.button("Increment Counter", on_click=increment_counter)
    st.button("Reset Counter", on_click=lambda: st.session_state.update(counter=0))
    st.subheader("Persisting Text Input")
    st.markdown("Text input that remembers its value even after other interactions.")
    if 'persisted_text' not in st.session_state:
        st.session_state.persisted_text = ""
    st.text_input(
        "Type something here:",
        key="text_input_widget", 
        on_change=update_text_input,
        value=st.session_state.persisted_text 
    )
    st.write(f"You typed (persisted): {st.session_state.persisted_text}")
    st.subheader("Widget State Association")
    st.markdown("Widgets with a `key` parameter automatically store their value in `st.session_state`.")
    st.slider("Select a value (with key)", 0, 10, 5, key="my_slider_state")
    st.write(f"Slider value from session state: {st.session_state.my_slider_state}")
    st.subheader("Inspecting Session State")
    st.write("You can view the entire `st.session_state` dictionary:")
    st.write(st.session_state)

elif demo_section == "Caching":
    st.header("8. Caching: Optimizing Performance")
    st.write("Caching helps speed up your app by storing results of expensive computations.")
    st.subheader("`@st.cache_data` for Data Loading")
    st.markdown("This caches the return value of functions that load or transform data. Each user gets their own cached copy.")
    st.write("Loading data... (This will be slow on first run, fast on subsequent runs)")
    data_loaded = load_expensive_data()
    st.dataframe(data_loaded.head())
    st.success("Data loaded (possibly from cache)!")

    st.subheader("`@st.cache_resource` for Global Resources")
    st.markdown("This caches global resources like ML models or database connections. The cached object is shared across all users and sessions.")
    st.write("Loading ML Model... (This will be slow on first app start, fast for all users/sessions)")
    model = load_expensive_model()
    st.write(f"Model loaded: {model}")
    st.success("Model loaded (possibly from cache)!")

    st.subheader("Clearing Cache")
    st.markdown("You can clear specific caches or all caches.")
    if st.button("Clear Data Cache (`@st.cache_data`)"):
        load_expensive_data.clear()
        st.info("`@st.cache_data` cleared. Next data load will be slow.")
    if st.button("Clear Resource Cache (`@st.cache_resource`)"):
        load_expensive_model.clear()
        st.info("`@st.cache_resource` cleared. Next model load will be slow.")
    if st.button("Clear ALL Caches"):
        st.cache_data.clear()
        st.cache_resource.clear()
        st.info("All caches cleared. All subsequent expensive operations will rerun.")

elif demo_section == "Status & Progress":
    st.header("9. Status and Progress Elements")
    st.write("Provide feedback to users about ongoing processes.")
    st.subheader("Progress Bar (`st.progress`)")
    st.markdown("Displays a progress bar for long-running operations.")
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()
    st.success("Operation complete!")
    st.subheader("Spinner (`st.spinner`)")
    st.markdown("Displays a spinner while a block of code is executing.")
    with st.spinner('Waiting for results...'):
        time.sleep(3)
    st.success("Done!")
    st.subheader("Status Messages")
    st.markdown("Provide quick feedback messages.")
    st.success("This is a success message!")
    st.info("This is an informational message.")
    st.warning("This is a warning message.")
    st.error("This is an error message!")
elif demo_section == "Custom Components":
    st.header("10. Custom Components: Extending Streamlit")
    st.write("For functionalities not natively supported, custom components allow integration of web technologies.")
    st.subheader("Embedding HTML (`st.components.v1.html`)")
    st.markdown("You can embed raw HTML directly into your app.")
    st.components.v1.html(
        """
        <div style=\"background-color: #f0f2f6; padding: 20px; border-radius: 10px;\">
          <h3 style=\"color: #333;\">Hello from Custom HTML!</h3>
          <p>This content is rendered directly from an HTML string.</p>
          <button onclick=\"alert('Button clicked in HTML!')\">Click Me</button>
        </div>
        """,
        height=150
    )
    st.subheader("Embedding Iframes (`st.components.v1.iframe`)")
    st.markdown("Embed content from other websites or local web apps via an iframe.")
    st.components.v1.iframe("https://docs.streamlit.io/get-started", height=400, scrolling=True)
    st.info("This iframe displays a section of the Streamlit documentation.")
    st.write("""
    For more complex, bi-directional custom components, you would typically develop
    a separate frontend (e.g., using React) and use `st.components.v1.declare_component`
    to establish communication between Python and JavaScript. This allows for
    infinite extensibility of Streamlit's capabilities.
    """)

elif demo_section == "Advanced & Experimental Features":
    st.header("11. Advanced & Experimental Features")
    st.write("Explore advanced, experimental, and less-common Streamlit features.")
    st.subheader("st.toast: Transient Notification")
    st.toast("This is a toast notification!", icon="🎉")
    st.subheader("st.exception: Display Exception Traceback")
    class DemoException(Exception):
        pass
    exc = DemoException("This is a demo exception for st.exception!")
    st.exception(exc)
    st.subheader("st.stop: Stop Script Execution")
    st.write("The code below will not run if you uncomment st.stop().")
    # st.stop()
    st.info("Uncomment st.stop() above to see script execution halt.")
    st.subheader("st.metric: KPI/Number Display")
    st.metric(label="Active Users", value=1234, delta="+56")
    st.metric(label="Conversion Rate", value="5.2%", delta="-0.3%", delta_color="inverse")
    st.subheader("st.empty: Dynamic Placeholder")
    placeholder = st.empty()
    if st.button("Show Dynamic Message in Placeholder"):
        placeholder.success("This message was inserted dynamically!")
    st.subheader("st.form with Multiple Submit Buttons")
    with st.form("multi_action_form"):
        a = st.text_input("Value A")
        b = st.text_input("Value B")
        submit1 = st.form_submit_button("Action 1")
        submit2 = st.form_submit_button("Action 2")
        if submit1:
            st.success(f"Action 1 submitted: {a}")
        if submit2:
            st.success(f"Action 2 submitted: {b}")
    st.subheader("st.form_submit_button with on_click")
    def on_form_submit():
        st.toast("Form submitted via on_click!", icon="✅")
    with st.form("form_on_click"):
        st.text_input("Type something")
        st.form_submit_button("Submit (on_click)", on_click=on_form_submit)
    st.subheader("st.write with Multiple Arguments/Objects")
    st.write("Multiple values:", 1, 2, 3, {"a": 10, "b": 20})
    st.write(pd.DataFrame({"A": [1,2], "B": [3,4]}), plt.figure())
    st.subheader("st.markdown with unsafe_allow_html")
    st.markdown('<span style="color: red; font-weight: bold;">This is red HTML text!</span>', unsafe_allow_html=True)
    st.subheader("st.columns with Unequal Widths")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.info("Wider column")
    with col2:
        st.warning("Narrower column")
    st.subheader("Nested st.container")
    with st.container():
        st.write("Outer container")
        with st.container():
            st.write("Inner container")
    st.subheader("st.caption for Images/Charts")
    st.image("https://picsum.photos/200", caption="Image with caption")
    st.caption("This is a caption for the image above.")
    st.subheader("st.download_button with Binary Data (Download Plot)")
    import io
    fig, ax = plt.subplots()
    ax.plot([0,1,2], [10,20,15])
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    st.download_button("Download Plot as PNG", data=buf.getvalue(), file_name="plot.png", mime="image/png")
    st.subheader("st.experimental_rerun")
    if st.button("Rerun App Now"):
        st.experimental_rerun()
    st.subheader("st.query_params (New API)")
    st.write("Current query params:", st.query_params)
    if st.button("Set Query Param foo=bar (New API)"):
        st.query_params["foo"] = "bar"
        st.info("Query param set! Reload to see effect.")
    if hasattr(st, "query_params"):
        st.subheader("st.query_params (New API)")
        st.write(st.query_params)
    st.subheader("st.secrets (Secure Credentials)")
    st.write("st.secrets is used for secure credentials. Example:")
    st.code("st.secrets['db_password'] # Add secrets in .streamlit/secrets.toml")
    if hasattr(st, "experimental_user"):
        st.subheader("st.experimental_user (User Info)")
        st.write(st.experimental_user)
    if hasattr(st, "experimental_connection"):
        st.subheader("st.experimental_connection (Database Connection)")
        st.write("See docs for usage.")
    st.subheader("st.session_state Callback with Arguments")
    def cb_with_args(arg):
        st.toast(f"Callback called with arg: {arg}")
    st.button("Callback with Arg", on_click=cb_with_args, args=("Hello!",))
    st.info("This section covers advanced and experimental Streamlit features. Some features may require the latest Streamlit version or special configuration.")