import streamlit as st

st.set_page_config(
    page_title="Road Damage Detections Apps",
    page_icon="🛣️",
)

st.divider()
st.title("Road Damage Detection Application")

st.markdown(
    """
    Introducing our Road Damage Detection Apps, powered by the YOLOv8 deep learning model trained on Custom Dataset.
    
    This application is designed to enhance road safety and infrastructure maintenance by swiftly identifying and categorizing various forms of road damage.

    There is four types of damage that this model can detects such as:
    - Cracks
    - Alligator Cracks
    - Potholes
    - Patching
    - Rutting

    You can select the apps from the sidebar to try and experiment with any kind of input **(realtime-webcam, video and images)** depends on your use case.

    #### Documentations and Links
    - Github Project Page [Github](https://github.com/achilis1505/RoadDamageDetection)
    - You can reach me on tasmiayemna@gmail.com

    #### License and Citations
    - All rights reserved on YOLOv8 license permits by [Ultralytics](https://github.com/ultralytics/ultralytics) and [Streamlit](https://streamlit.io/) framework
"""
)
