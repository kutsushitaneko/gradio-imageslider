import gradio as gr

def create_imageslider():
    # 画像のパスを設定
    image_paths = (
        "palepink.png",
        "black_and_white.png"
    )
    
    # Gradioアプリの作成
    with gr.Blocks() as demo:
        gr.ImageSlider(
            label="イメージスライダーデモ",
            show_label=True,
            value=image_paths,
        )
    
    return demo

if __name__ == "__main__":
    demo = create_imageslider()
    demo.launch(
        inbrowser=True,
        show_error=True
    )
