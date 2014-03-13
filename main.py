# -*- coding: UTF-8 -*-
'''
Created on 2014-03-13

@author: Grayson
'''
import lottery, collections

if __name__ == '__main__':
  html = lottery.getUrlResponse('http://datachart.500.com/ssq/history/inc/history.php?limit=10000&referrer=')
  winningInfo = lottery.matchWinningLine(html)
  redBallDict = collections.OrderedDict()
  for i in range(1, 34):
    if (i < 10):
      redBallDict['0' + str(i)] = 0
    else:
      redBallDict[str(i)] = 0
  blueBallDict = collections.OrderedDict()
  for i in range(1, 17):
    if (i < 10):
      blueBallDict['0' + str(i)] = 0
    else:
      blueBallDict[str(i)] = 0
  if (winningInfo is not None):
    winningDict = lottery.getWinningInfo(winningInfo)
    winningCount = len(winningDict)
    print 'winningCount: ', winningCount
    for winning in winningDict:
      for redBall in winningDict[winning]['RB']:
        redBallDict[redBall] += winningCount
      blueBallDict[winningDict[winning]['BB']] += winningCount
      winningCount -= 1
    sortedRedBall = sorted(redBallDict.items(), key=lambda d:d[1], reverse=True)
    sortedBlueBall = sorted(blueBallDict.items(), key=lambda d:d[1], reverse=True)
    #print 'sortedRedBall: ', sortedRedBall
    #print 'blueBallDict: ', sortedBlueBall
    redBallList = list()
    for redBall in sortedRedBall:
      if (len(redBallList) < 6):
        redBallList.append(redBall[0])
      else:
        break
    redBallList.sort()
    print 'Red Ball: ' + str(redBallList) + ', Blue Ball:[\'' + str(sortedBlueBall[0][0]) + '\']. Buy it, and now!!!'


  else:
    print 'None'
