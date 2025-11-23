import gradio as gr
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text):
    """
    Generates a word cloud from the input text and returns a matplotlib figure.
    """
    if not text.strip():
        # Handle empty text input gracefully
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.text(0.5, 0.5, "Please enter some text to generate a word cloud.",
                horizontalalignment='center', verticalalignment='center',
                fontsize=12, color='red')
        ax.axis('off')
        return fig

    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Create a matplotlib figure and display the word cloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off') # Remove axes
    return fig

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_wordcloud,
    inputs=gr.Textbox(lines=5, label="Enter your text here", placeholder="Type or paste text to generate a word cloud..."),
    outputs=gr.Plot(label="Generated Word Cloud"),
    title="Word Cloud Generator",
    description="Enter any text below to generate a visual word cloud based on the frequency of words. Leave blank for an example."
)

# Launch the Gradio application
if __name__ == "__main__":
    iface.launch()
