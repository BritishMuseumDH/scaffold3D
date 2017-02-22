[![ORCiD](https://img.shields.io/badge/ORCiD-0000--0002--0246--2335-green.svg)](http://orcid.org/0000-0002-0246-2335)

# Scaffold a 3D folder directory

A very simple python script to set up the directory format for adding 3D data to Github.

The @britishmuseum license terms are CC-BY-NC-SA.

# Structure created

Each project you scaffold will create the following directory structure:

<pre>
/[projectname]/
/[projectname]/images
/[projectname]/masks
/[projectname]/models
/[projectname]/.gitignore
/[projectname]/readme.md
/[projectname]/LICENSE.md
</pre>

When you come to add data to the project, you will need to put raw images for 3D into the images folder and then the
other folders will be populated when you create masks and models within PhotoScan.

# Running Scaffold3D script

To run this (tested on OSX only) issue following command in terminal:

<pre>python make3D.py -p 'projectname' -wd '/Users/Danielpett/githubProjects/' </pre>

# License

CC0
