# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Scipy Lecture Notes
# %% [markdown]
# ## 一份文档，帮助你熟悉Python的数值，科学以及数据处理生态。
# %% [markdown]
# 这是一份Python数据处理的指南。它包括，但不仅限于Python科学计算，数据处理相关的核心工具和技巧。 它由易到难，每一个章节都对应着1~2个小时的课程。我们相信不同水平的读者都可以从这份指南中获益。

# %%
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y)

# %% [markdown]
# \begin{equation}
#   y = \sin(x)
# \end{equation}

# %%
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
z = np.cos(x)
plt.plot(x,z)

# %% [markdown]
# \begin{equation}
#   z = \cos(x)
# \end{equation}

