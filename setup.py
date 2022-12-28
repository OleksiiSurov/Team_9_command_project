from setuptools import setup, find_namespace_packages
setup(
      name='smart_bot',
      version='1.0.0',
      description='bot with the functions of adding notes and sorting folders',
      url='https://github.com/OleksiiSurov/Team_9_command_project/tree/main',
      author='30 seconds to mars code',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['bot = smartBot.main:main']},
      )
