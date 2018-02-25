
# coding: utf-8

# # Lab 0: Introduction and Practice with Jupyter Notebooks

# Welcome to Data 8X: Foundations of Data Science!  Each week you will complete a lab assignment in a jupyter notebook.
# 
# In Lab 0, you will learn how to navigate a Jupyter Notebook (like this one). You will be completeling all your lab assignments in jupyter notebooks, so it's important that you learn how to navigate a jupyter notebook.  Let's get started!

# ## 1. Jupyter notebooks
# This webpage is called a Jupyter notebook. A notebook is a place to write programs and view their results.
# 
# ### 1.1. Text cells
# In a notebook, each rectangle containing text or code is called a *cell*.
# 
# Text cells (like this one) can be edited by double-clicking on them. They're written in a simple format called [Markdown](http://daringfireball.net/projects/markdown/syntax) to add formatting and section headings.  You don't need to learn Markdown, but you might want to.
# 
# After you edit a text cell, click the "run cell" button at the top that looks like ▶| to confirm any changes. (Try not to delete the instructions of the lab.)

# **Question 1.1.1.** <br />
# This paragraph is in its own text cell.  Try editing it so that this sentence is the last sentence in the paragraph, and then click the "run cell" ▶| button on the top.  This sentence, for example, should be deleted.  So should this one.

# In[ ]:


print("Hello, World!")


# And this one:

# In[ ]:


print("\N{WAVING HAND SIGN}, \N{EARTH GLOBE ASIA-AUSTRALIA}!")


# The fundamental building block of Python code is an expression. Cells can contain multiple lines with multiple expressions. When you run a cell, the lines of code are executed in the order in which they appear. Every `print` expression prints a line. Run the next cell and notice the order of the output.

# In[ ]:


print("First this line is printed,")
print("and then this one.")


# **Question 1.2.1.** <br />
# Change the cell above so that it prints out:
# 
#     First this line,
#     then the whole 🌏,
#     and then this one.
# 
# *Hint:* If you're stuck on the Earth symbol for more than a few minutes, try looking at previous print statement

# ### 1.3. Writing Jupyter notebooks
# You can use Jupyter notebooks for your own projects or documents.  When you make your own notebook, you'll need to create your own cells for text and code.
# 
# To add a cell, click the + button in the menu bar.  It'll start out as a text cell.  You can change it to a code cell by clicking inside it so it's highlighted, clicking the drop-down box next to the restart (⟳) button in the menu bar, and choosing "Code".
# 
# **Question 1.3.1.** <br />
# Add a code cell below this one.  Write code in it that prints out:
#    
#     A whole new cell! ♪🌏♪
# 
# (That musical note symbol is like the Earth symbol.  Its long-form name is `\N{EIGHTH NOTE}`.)
# 
# Run your cell to verify that it works.

# ### 1.4. Errors
# Python is a language, and like natural human languages, it has rules.  It differs from natural language in two important ways:
# 1. The rules are *simple*.  You can learn most of them in a few weeks and gain reasonable proficiency with the language in a semester.
# 2. The rules are *rigid*.  If you're proficient in a natural language, you can understand a non-proficient speaker, glossing over small mistakes.  A computer running Python code is not smart enough to do that.
# 
# Whenever you write code, you'll make mistakes.  When you run a code cell that has errors, Python will sometimes produce error messages to tell you what you did wrong.
# 
# Errors are okay; even experienced programmers make many errors.  When you make an error, you just have to find the source of the problem, fix it, and move on.
# 
# We have made an error in the next cell.  Run it and see what happens.

# In[ ]:


print("This line is missing something."print("This line is missing something.")


# You should see something like this (minus our annotations):
# 
# <img src="error.jpg" alt=""/>
# 
# The last line of the error output attempts to tell you what went wrong.  The *syntax* of a language is its structure, and this `SyntaxError` tells you that you have created an illegal structure.  "`EOF`" means "end of file," so the message is saying Python expected you to write something more (in this case, a right parenthesis) before finishing the cell.
# 
# There's a lot of terminology in programming languages, but you don't need to know it all in order to program effectively. If you see a cryptic message like this, you can often get by without deciphering it.
# 
# Try to fix the code above so that you can run the cell and see the intended message instead of an error.

# ### 1.5. The Kernel
# The kernel is a program that executes the code inside your notebook and outputs the results. In the top right of your window, you can see a circle that indicates the status of your kernel. If the circle is empty (⚪), the kernel is idle and ready to execute code. If the circle is filled in (⚫), the kernel is busy running some code. 
# 
# You may run into problems where your kernel is stuck for an excessive amount of time, your notebook is very slow and unresponsive, or your kernel loses its connection. If this happens, try the following steps:
# 1. At the top of your screen, click **Kernel**, then **Interrupt**.
# 2. If that doesn't help, click **Kernel**, then **Restart**. If you do this, you will have to run your code cells from the start of your notebook up until where you paused your work.
# 3. If that doesn't help, restart your server. First, save your work by clicking **File** at the top left of your screen, then **Save and Checkpoint**. Next, click **Control Panel** at the top right. Choose **Stop My Server** to shut it down, then **My Server** to start it back up. Then, navigate back to the notebook you were working on.

# ### 1.6. Submitting your work
# All assignments in the course will be distributed as notebooks like this one, and you will submit your work from the notebook. We will use a system called OK that checks your work and helps you submit. At the top of each assignment, you'll see a cell like the one below that prompts you to identify yourself. Run it to import your autograder tests.

# In[ ]:


# Don't change this cell; just run it.
# These statments import 
from client.api.notebook import Notebook
ok = Notebook('lab00.ok')


# When you finish a question, you need to check your answer by running the grade command below. It's OK to grade multiple times, OK will only try to grade your final submission for each question.

# In[ ]:


_ = ok.grade("q0")

