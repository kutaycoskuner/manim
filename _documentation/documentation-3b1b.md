- This is fork of original manim from 3b1b github repository.  

- fork date is 20260109

- i started creating virtual env first  
py -m venv .venv

- activate venv  
.venv\Scripts\activate

- installing engine (editable mode)  
pip install -e .
    - pip reads the project’s metadata (setup.py / pyproject.toml) in the current directory (.) and makes it importable:  

- testing if install successfull  
manimgl --version  

- requirements  
    - ffmpeg
    - opengl
    - latex (optional)

- created test/test_dot.py
- run created
manimgl test_dot.py Minimal

- created test/test_coords.py
manimgl test_coords.py FunctionPlot