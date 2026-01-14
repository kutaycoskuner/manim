
1. create virtual environment
```bash
python -m venv .venv
```

2. activate virtual environment
```bash
.venv\Scripts\activate
```

3. intall manim communtiy
```bash
# install
pip install manim
# to check version
manim --version
## you should see something like Manim Community v0.19.1
```

4. following the initial tutorial on 
    - https://docs.manim.community/en/stable/tutorials/quickstart.html
```bash
# on root 
# remark: they have changed the default version so there is different drawing on first tutorial.
# I changed it to be the same with on tutoraial page.
manim init project my-project --default 
# go to project folder
cd my-project
# and run
manim -pql main.py CreateCircle
```

```bash
-p          # preview after render
-ql         # low quality fast
manim -pql uniform_convergence/main.py uniform_convergence --format gif --transparent
```