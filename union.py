<<<<<<< HEAD
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        s1=set(a)
        s2=set(b)
        s3=s1 | s2
        return len(s3)
=======
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMD+sbrx98dpMIkducxN2DB",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/EliasSf73/Competitive_programming_submission/blob/main/union.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "_sCXD5lE02ve"
      },
      "outputs": [],
      "source": [
        "class Solution:\n",
        "    #Function to return the count of number of elements in union of two arrays.\n",
        "    def doUnion(self,a,n,b,m):\n",
        "\n",
        "        #code here\n",
        "        s1=set(a)\n",
        "        s2=set(b)\n",
        "        s3=s1 | s2\n",
        "        return len(s3)"
      ]
    }
  ]
}
>>>>>>> 44aa0ef00b9a26e959699061b5dbb64f04817cb6
