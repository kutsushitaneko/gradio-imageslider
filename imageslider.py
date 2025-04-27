import gradio as gr
from PIL import Image

def create_imageslider():
    # 画像のパスを設定
    image_paths = (
        "images/palepink.png",
        "images/black_and_white.png"
    )
    
    # Gradioアプリの作成
    with gr.Blocks() as demo:
        gr.ImageSlider(
            label="イメージスライダーデモ",
            value=image_paths,  # 画像パスのタプルを渡す
            show_label=True,
            container=True
        )
    
    return demo

if __name__ == "__main__":
    demo = create_imageslider()
    demo.launch(
        inbrowser=True,  # ブラウザを自動的に開く
        show_error=True  # エラーを表示
    )
