import os, uuid, boto3
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreatView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required