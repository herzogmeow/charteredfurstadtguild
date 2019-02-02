import CoreSystem
import DungeonCoreSystem
import MemberList
import BoardGuilds

chartered = CharteredGuild("Chartered Furstadt Guild")

chartered.member.load(memberList,"Member")
chartered.member.load(boardGuilds, "BoardGuilds")

def Rule_Change(Pull_Request):
  AssemblyDecision = false
  BoardGuildDecision = false
  Assembly = chartered.member("Member")
  BoardofGuilds = chartered.member("BoardGuilds")
  TimeDiff = SystemTime.now() - Pull_Request.systime()
  if (Assembly.votes() > Assembly.total() * 0.1) and (Assembly.votes("agree") > Assembly.votes("disagree") and TimeDiff.morethan("8H")):
    AssemblyDecision = true
  if (BoardofGuilds.votes("agree") > BoardofGuilds.votes("disagree") and TimeDiff.morethan("8H")):
    BoardGuildDecision = true
  if (AssemblyDecision and BoardGuildDecision):
    chartered.rulechange(Pull_Request)

if chartered.has_pullRequest:
  listPullRequest = chartered.pullrequest.waiting()
  for Pull_Request in listPullRequest:
    Rule_Change(Pull_Request)
    if Pull_Request.maxTime() > SystemTime.now():
      Pull_Request.dismiss()
