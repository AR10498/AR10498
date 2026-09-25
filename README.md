# AR10498
Python Lesson Notebooks

Clone in Notebooks with:  
1. From the start menu (or mac launcher) Open Anaconda Navigator (Python 3), then JupyterLab
2. Start a new Notebook (Python 3) and cut/paste and run the following line of code exactly as is:
```python
%pip install pygit2
```
3. Restart the kernel (⟳) and copy and run this whole block in a blank cell:
```python
import pygit2

pygit2.clone_repository('https://github.com/AR10498/AR10498.git', 'AR10498')
```
4. This should copy the course materials to your workspace.
