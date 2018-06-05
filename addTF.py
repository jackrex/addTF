#!/usr/bin/python
#coding:utf-8
__author__ = 'jackrex'

from flask import Flask
from flask import render_template
from flask import request
from Naked.toolshed.shell import muterun_rb
import os

app = Flask(__name__)

result_str = ''

@app.route('/')
def addUdid():
    return render_template('upload.html')


@app.route('/author')
def author():
    return 'Made By Jackrex'

@app.route('/addTF', methods=['POST', 'GET'])
def call_add_tf_ruby():
    email = request.form['email']
    print ('email' + email)
    #success = muterun_rb('udid.rb', email)
    cmd = "fastlane pilot add " + email + " -a com.gotokeep.keep.intl --username keepvendors@gmail.com -g BetaUsers"
    success = os.system(cmd)
    print('returned value:', success)

    global result_str
    if success == 0:
        print ('success')
        result_str = u'提交成功:'
    else:
        print ('error \n')
        result_str = u'提交失败:'

    return render_template('result.html', result=result_str)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

