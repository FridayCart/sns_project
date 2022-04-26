from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response, Response
import twitter
import jwt
import datetime
import base64
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ckart.db'
app.config['SECRET_KEY'] = 'thisisasecret'



@app.route('/', methods=['POST'])
def show_details():
    api_key= ''
    api_secret_key= ''
    access_token= ''
    access_secret_token= ''
    a1=request.form.get('search')
    a=twitter.Api(consumer_key=api_key,consumer_secret=api_secret_key,access_token_key=access_token,access_token_secret=access_secret_token)
    '''b=a.VerifyCredentials()
    b=b.AsDict()'''
    
    b=a.GetUser(screen_name=a1)
    b=b.AsDict()
    if not b:
        flash('Invalid User','error')
    return render_template('home.html',det=b)

@app.route('/')
def show_details_get():
    det={
    'created_at': 'Fri Apr 08 12:39:50 +0000 2022',
    'default_profile': True,
    'favourites_count': 1,
    'followers_count': 2,
    'friends_count': 7,
    'id': 1512409846729289737,
    'id_str': '1512409846729289737',
    'name': 'kick hamilton',
    'profile_background_color': 'F5F8FA',
    'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1512409846729289737/1650885555',
    'profile_image_url': 'http://pbs.twimg.com/profile_images/1518549995540127744/bWd-AyS__normal.jpg',
    'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1518549995540127744/bWd-AyS__normal.jpg',
    'profile_link_color': '1DA1F2',
    'profile_sidebar_border_color': 'C0DEED',
    'profile_sidebar_fill_color': 'DDEEF6',
    'profile_text_color': '333333',
    'profile_use_background_image': True,
    'screen_name': 'hamilton_kick',
    'withheld_in_countries': []
    }
    return render_template('home.html',det=det)

@app.route('/show')
def show_details_get1():
    api_key= ''
    api_secret_key= ''
    access_token= ''
    access_secret_token= ''
    a1=request.form.get('search')
    a=twitter.Api(consumer_key=api_key,consumer_secret=api_secret_key,access_token_key=access_token,access_token_secret=access_secret_token)
    brr = a.GetFollowers()
    a11=[]
    for i in brr:
        a11.append(i.AsDict()['screen_name'])
    det1=[]
    for x in a11:
        b=a.GetUser(screen_name=x).AsDict()
        det1.append(b)
    pp={
    'created_at': 'Fri Apr 08 12:39:50 +0000 2022',
    'default_profile': True,
    'favourites_count': 1,
    'followers_count': 2,
    'friends_count': 7,
    'id': 1512409846729289737,
    'id_str': '1512409846729289737',
    'name': 'kick hamilton',
    'profile_background_color': 'F5F8FA',
    'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1512409846729289737/1650885555',
    'profile_image_url': 'http://pbs.twimg.com/profile_images/1518549995540127744/bWd-AyS__normal.jpg',
    'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1518549995540127744/bWd-AyS__normal.jpg',
    'profile_link_color': '1DA1F2',
    'profile_sidebar_border_color': 'C0DEED',
    'profile_sidebar_fill_color': 'DDEEF6',
    'profile_text_color': '333333',
    'profile_use_background_image': True,
    'screen_name': 'hamilton_kick',
    'withheld_in_countries': []
    }
    return render_template('index.html',det1=det1,pp=pp)
