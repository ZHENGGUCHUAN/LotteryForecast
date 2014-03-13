# -*- coding: UTF-8 -*-
'''
Created on 2014-03-13

@author: Grayson
'''
import urllib2, re, collections

def getUrlResponse(url):
  '''
  从指定URL获取全部http返回信息
  '''
  request = urllib2.Request(url)
  response = urllib2.urlopen(request)
  html = response.read()
  return html


def matchWinningLine(html):
  '''
  完整字符串以换行符分割，并定位查询指定标头信息。
  '''
  lineList = html.split('\n')
  pattern = re.compile(r'<tr class="t_tr1"><!--<td>2</td>--><td>')
  for line in lineList:
    if (pattern.match(line.strip()) is not None):
      return line.strip()
  return None


def getPhaseNum(phaseNumStr):
  phaseNum = phaseNumStr.replace('<!--<td>2</td>--><td>', '')
  phaseNum = phaseNum.replace('</td>', '')
  return phaseNum


def getRedBall(redBallStrList):
  redBall = list()
  for redBallStr in redBallStrList:
    redBallStr = redBallStr.replace('<td class="t_cfont2">', '')
    redBallStr = redBallStr.replace('</td>', '')
    redBall.append(redBallStr)
  return redBall


def getBlueBall(blueBallStr):
  blueBall = blueBallStr.replace('<td class="t_cfont4">', '')
  blueBall = blueBall.replace('</td>', '')
  return blueBall


def getWinningInfo(winningLine):
  '''
  获取每一期具体信息
  {<phase num>:{'RB':[<red ball list>], 'BB':<blue ball>}}
  '''
  phaseList = winningLine.strip().split('<tr class="t_tr1">')
  phaseNumPattern = re.compile('<!--<td>2</td>--><td>\d*</td>')
  redBallPattern = re.compile('<td class="t_cfont2">\d{2}</td>')
  blueBallPattern = re.compile('<td class="t_cfont4">\d{2}</td>')
  phaseDict = collections.OrderedDict()
  for phase in phaseList:
    #去除无效行记录
    if (phase == ''):
      continue
    #期数匹配
    phaseNumStr = phaseNumPattern.search(phase)
    phaseNum = getPhaseNum(phaseNumStr.group())
    #print 'phaseNum: ', phaseNum
    #红球匹配
    redBallStrList = redBallPattern.findall(phase)
    redBall = getRedBall(redBallStrList)
    #print 'redBall: ', redBall
    #蓝球匹配
    blueBallStr = blueBallPattern.search(phase)
    blueBall = getBlueBall(blueBallStr.group())
    #print 'blueBall: ', blueBall
    phaseDict[phaseNum] = {'RB':redBall, 'BB':blueBall}
  return phaseDict
