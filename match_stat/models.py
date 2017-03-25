from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MatchInfo(models.Model):

    matchid=models.BigIntegerField(primary_key=True,unique=True)
    info_type=models.CharField(max_length=12,blank=True,null=True)
    info_date=models.DateTimeField(blank=True,null=True)
    info_time=models.TimeField(blank=True,null=True)
    info_playtime=models.TimeField(blank=True,null=True)

    player1_resault=models.CharField(max_length=12,blank=True,null=True)
    player1_name=models.CharField(max_length=32,blank=True,null=True)
    player1_hero=models.CharField(max_length=32,blank=True,null=True)
    player1_kills=models.IntegerField(blank=True,null=True)
    player1_dies=models.IntegerField(blank=True,null=True)
    player1_helps=models.IntegerField(blank=True,null=True)
    player1_wins=models.CharField(max_length=12,blank=True,null=True)
    player1_soldiers=models.IntegerField(blank=True,null=True)
    player1_golds=models.IntegerField(blank=True,null=True)
    player1_skill1=models.CharField(max_length=12,blank=True,null=True)
    player1_skill2=models.CharField(max_length=12,blank=True,null=True)
    player1_item1=models.CharField(max_length=64,blank=True,null=True)
    player1_item2=models.CharField(max_length=64,blank=True,null=True)
    player1_item3=models.CharField(max_length=64,blank=True,null=True)
    player1_item4=models.CharField(max_length=64,blank=True,null=True)
    player1_item5=models.CharField(max_length=64,blank=True,null=True)
    player1_item6=models.CharField(max_length=64,blank=True,null=True)
    player1_gain_golds=models.IntegerField(blank=True,null=True)
    player1_gain_exp=models.IntegerField(blank=True,null=True)
    player1_jiecao=models.BigIntegerField(blank=True,null=True)
    player1_win_p=models.CharField(max_length=32,blank=True,null=True)

    player2_resault=models.CharField(max_length=12,blank=True,null=True)
    player2_name=models.CharField(max_length=32,blank=True,null=True)
    player2_hero=models.CharField(max_length=32,blank=True,null=True)
    player2_kills=models.IntegerField(blank=True,null=True)
    player2_dies=models.IntegerField(blank=True,null=True)
    player2_helps=models.IntegerField(blank=True,null=True)
    player2_wins=models.CharField(max_length=12,blank=True,null=True)
    player2_soldiers=models.IntegerField(blank=True,null=True)
    player2_golds=models.IntegerField(blank=True,null=True)
    player2_skill1=models.CharField(max_length=12,blank=True,null=True)
    player2_skill2=models.CharField(max_length=12,blank=True,null=True)
    player2_item1=models.CharField(max_length=64,blank=True,null=True)
    player2_item2=models.CharField(max_length=64,blank=True,null=True)
    player2_item3=models.CharField(max_length=64,blank=True,null=True)
    player2_item4=models.CharField(max_length=64,blank=True,null=True)
    player2_item5=models.CharField(max_length=64,blank=True,null=True)
    player2_item6=models.CharField(max_length=64,blank=True,null=True)
    player2_gain_golds=models.IntegerField(blank=True,null=True)
    player2_gain_exp=models.IntegerField(blank=True,null=True)
    player2_jiecao=models.BigIntegerField(blank=True,null=True)
    player2_win_p=models.CharField(max_length=32,blank=True,null=True)

    player3_resault=models.CharField(max_length=12,blank=True,null=True)
    player3_name=models.CharField(max_length=32,blank=True,null=True)
    player3_hero=models.CharField(max_length=32,blank=True,null=True)
    player3_kills=models.IntegerField(blank=True,null=True)
    player3_dies=models.IntegerField(blank=True,null=True)
    player3_helps=models.IntegerField(blank=True,null=True)
    player3_wins=models.CharField(max_length=12,blank=True,null=True)
    player3_soldiers=models.IntegerField(blank=True,null=True)
    player3_golds=models.IntegerField(blank=True,null=True)
    player3_skill1=models.CharField(max_length=12,blank=True,null=True)
    player3_skill2=models.CharField(max_length=12,blank=True,null=True)
    player3_item1=models.CharField(max_length=64,blank=True,null=True)
    player3_item2=models.CharField(max_length=64,blank=True,null=True)
    player3_item3=models.CharField(max_length=64,blank=True,null=True)
    player3_item4=models.CharField(max_length=64,blank=True,null=True)
    player3_item5=models.CharField(max_length=64,blank=True,null=True)
    player3_item6=models.CharField(max_length=64,blank=True,null=True)
    player3_gain_golds=models.IntegerField(blank=True,null=True)
    player3_gain_exp=models.IntegerField(blank=True,null=True)
    player3_jiecao=models.BigIntegerField(blank=True,null=True)
    player3_win_p=models.CharField(max_length=32,blank=True,null=True)

    player4_resault=models.CharField(max_length=12,blank=True,null=True)
    player4_name=models.CharField(max_length=32,blank=True,null=True)
    player4_hero=models.CharField(max_length=32,blank=True,null=True)
    player4_kills=models.IntegerField(blank=True,null=True)
    player4_dies=models.IntegerField(blank=True,null=True)
    player4_helps=models.IntegerField(blank=True,null=True)
    player4_wins=models.CharField(max_length=12,blank=True,null=True)
    player4_soldiers=models.IntegerField(blank=True,null=True)
    player4_golds=models.IntegerField(blank=True,null=True)
    player4_skill1=models.CharField(max_length=12,blank=True,null=True)
    player4_skill2=models.CharField(max_length=12,blank=True,null=True)
    player4_item1=models.CharField(max_length=64,blank=True,null=True)
    player4_item2=models.CharField(max_length=64,blank=True,null=True)
    player4_item3=models.CharField(max_length=64,blank=True,null=True)
    player4_item4=models.CharField(max_length=64,blank=True,null=True)
    player4_item5=models.CharField(max_length=64,blank=True,null=True)
    player4_item6=models.CharField(max_length=64,blank=True,null=True)
    player4_gain_golds=models.IntegerField(blank=True,null=True)
    player4_gain_exp=models.IntegerField(blank=True,null=True)
    player4_jiecao=models.BigIntegerField(blank=True,null=True)
    player4_win_p=models.CharField(max_length=32,blank=True,null=True)

    player5_resault=models.CharField(max_length=12,blank=True,null=True)
    player5_name=models.CharField(max_length=32,blank=True,null=True)
    player5_hero=models.CharField(max_length=32,blank=True,null=True)
    player5_kills=models.IntegerField(blank=True,null=True)
    player5_dies=models.IntegerField(blank=True,null=True)
    player5_helps=models.IntegerField(blank=True,null=True)
    player5_wins=models.CharField(max_length=12,blank=True,null=True)
    player5_soldiers=models.IntegerField(blank=True,null=True)
    player5_golds=models.IntegerField(blank=True,null=True)
    player5_skill1=models.CharField(max_length=12,blank=True,null=True)
    player5_skill2=models.CharField(max_length=12,blank=True,null=True)
    player5_item1=models.CharField(max_length=64,blank=True,null=True)
    player5_item2=models.CharField(max_length=64,blank=True,null=True)
    player5_item3=models.CharField(max_length=64,blank=True,null=True)
    player5_item4=models.CharField(max_length=64,blank=True,null=True)
    player5_item5=models.CharField(max_length=64,blank=True,null=True)
    player5_item6=models.CharField(max_length=64,blank=True,null=True)
    player5_gain_golds=models.IntegerField(blank=True,null=True)
    player5_gain_exp=models.IntegerField(blank=True,null=True)
    player5_jiecao=models.BigIntegerField(blank=True,null=True)
    player5_win_p=models.CharField(max_length=32,blank=True,null=True)

    player6_resault=models.CharField(max_length=12,blank=True,null=True)
    player6_name=models.CharField(max_length=32,blank=True,null=True)
    player6_hero=models.CharField(max_length=32,blank=True,null=True)
    player6_kills=models.IntegerField(blank=True,null=True)
    player6_dies=models.IntegerField(blank=True,null=True)
    player6_helps=models.IntegerField(blank=True,null=True)
    player6_wins=models.CharField(max_length=12,blank=True,null=True)
    player6_soldiers=models.IntegerField(blank=True,null=True)
    player6_golds=models.IntegerField(blank=True,null=True)
    player6_skill1=models.CharField(max_length=12,blank=True,null=True)
    player6_skill2=models.CharField(max_length=12,blank=True,null=True)
    player6_item1=models.CharField(max_length=64,blank=True,null=True)
    player6_item2=models.CharField(max_length=64,blank=True,null=True)
    player6_item3=models.CharField(max_length=64,blank=True,null=True)
    player6_item4=models.CharField(max_length=64,blank=True,null=True)
    player6_item5=models.CharField(max_length=64,blank=True,null=True)
    player6_item6=models.CharField(max_length=64,blank=True,null=True)
    player6_gain_golds=models.IntegerField(blank=True,null=True)
    player6_gain_exp=models.IntegerField(blank=True,null=True)
    player6_jiecao=models.BigIntegerField(blank=True,null=True)
    player6_win_p=models.CharField(max_length=32,blank=True,null=True)

    player7_resault=models.CharField(max_length=12,blank=True,null=True)
    player7_name=models.CharField(max_length=32,blank=True,null=True)
    player7_hero=models.CharField(max_length=32,blank=True,null=True)
    player7_kills=models.IntegerField(blank=True,null=True)
    player7_dies=models.IntegerField(blank=True,null=True)
    player7_helps=models.IntegerField(blank=True,null=True)
    player7_wins=models.CharField(max_length=12,blank=True,null=True)
    player7_soldiers=models.IntegerField(blank=True,null=True)
    player7_golds=models.IntegerField(blank=True,null=True)
    player7_skill1=models.CharField(max_length=12,blank=True,null=True)
    player7_skill2=models.CharField(max_length=12,blank=True,null=True)
    player7_item1=models.CharField(max_length=64,blank=True,null=True)
    player7_item2=models.CharField(max_length=64,blank=True,null=True)
    player7_item3=models.CharField(max_length=64,blank=True,null=True)
    player7_item4=models.CharField(max_length=64,blank=True,null=True)
    player7_item5=models.CharField(max_length=64,blank=True,null=True)
    player7_item6=models.CharField(max_length=64,blank=True,null=True)
    player7_gain_golds=models.IntegerField(blank=True,null=True)
    player7_gain_exp=models.IntegerField(blank=True,null=True)
    player7_jiecao=models.BigIntegerField(blank=True,null=True)
    player7_win_p=models.CharField(max_length=32,blank=True,null=True)

    player8_resault=models.CharField(max_length=12,blank=True,null=True)
    player8_name=models.CharField(max_length=32,blank=True,null=True)
    player8_hero=models.CharField(max_length=32,blank=True,null=True)
    player8_kills=models.IntegerField(blank=True,null=True)
    player8_dies=models.IntegerField(blank=True,null=True)
    player8_helps=models.IntegerField(blank=True,null=True)
    player8_wins=models.CharField(max_length=12,blank=True,null=True)
    player8_soldiers=models.IntegerField(blank=True,null=True)
    player8_golds=models.IntegerField(blank=True,null=True)
    player8_skill1=models.CharField(max_length=12,blank=True,null=True)
    player8_skill2=models.CharField(max_length=12,blank=True,null=True)
    player8_item1=models.CharField(max_length=64,blank=True,null=True)
    player8_item2=models.CharField(max_length=64,blank=True,null=True)
    player8_item3=models.CharField(max_length=64,blank=True,null=True)
    player8_item4=models.CharField(max_length=64,blank=True,null=True)
    player8_item5=models.CharField(max_length=64,blank=True,null=True)
    player8_item6=models.CharField(max_length=64,blank=True,null=True)
    player8_gain_golds=models.IntegerField(blank=True,null=True)
    player8_gain_exp=models.IntegerField(blank=True,null=True)
    player8_jiecao=models.BigIntegerField(blank=True,null=True)
    player8_win_p=models.CharField(max_length=32,blank=True,null=True)

    player9_resault=models.CharField(max_length=12,blank=True,null=True)
    player9_name=models.CharField(max_length=32,blank=True,null=True)
    player9_hero=models.CharField(max_length=32,blank=True,null=True)
    player9_kills=models.IntegerField(blank=True,null=True)
    player9_dies=models.IntegerField(blank=True,null=True)
    player9_helps=models.IntegerField(blank=True,null=True)
    player9_wins=models.CharField(max_length=12,blank=True,null=True)
    player9_soldiers=models.IntegerField(blank=True,null=True)
    player9_golds=models.IntegerField(blank=True,null=True)
    player9_skill1=models.CharField(max_length=12,blank=True,null=True)
    player9_skill2=models.CharField(max_length=12,blank=True,null=True)
    player9_item1=models.CharField(max_length=64,blank=True,null=True)
    player9_item2=models.CharField(max_length=64,blank=True,null=True)
    player9_item3=models.CharField(max_length=64,blank=True,null=True)
    player9_item4=models.CharField(max_length=64,blank=True,null=True)
    player9_item5=models.CharField(max_length=64,blank=True,null=True)
    player9_item6=models.CharField(max_length=64,blank=True,null=True)
    player9_gain_golds=models.IntegerField(blank=True,null=True)
    player9_gain_exp=models.IntegerField(blank=True,null=True)
    player9_jiecao=models.BigIntegerField(blank=True,null=True)
    player9_win_p=models.CharField(max_length=32,blank=True,null=True)

    player10_resault=models.CharField(max_length=12,blank=True,null=True)
    player10_name=models.CharField(max_length=32,blank=True,null=True)
    player10_hero=models.CharField(max_length=32,blank=True,null=True)
    player10_kills=models.IntegerField(blank=True,null=True)
    player10_dies=models.IntegerField(blank=True,null=True)
    player10_helps=models.IntegerField(blank=True,null=True)
    player10_wins=models.CharField(max_length=12,blank=True,null=True)
    player10_soldiers=models.IntegerField(blank=True,null=True)
    player10_golds=models.IntegerField(blank=True,null=True)
    player10_skill1=models.CharField(max_length=12,blank=True,null=True)
    player10_skill2=models.CharField(max_length=12,blank=True,null=True)
    player10_item1=models.CharField(max_length=64,blank=True,null=True)
    player10_item2=models.CharField(max_length=64,blank=True,null=True)
    player10_item3=models.CharField(max_length=64,blank=True,null=True)
    player10_item4=models.CharField(max_length=64,blank=True,null=True)
    player10_item5=models.CharField(max_length=64,blank=True,null=True)
    player10_item6=models.CharField(max_length=64,blank=True,null=True)
    player10_gain_golds=models.IntegerField(blank=True,null=True)
    player10_gain_exp=models.IntegerField(blank=True,null=True)
    player10_jiecao=models.BigIntegerField(blank=True,null=True)
    player10_win_p=models.CharField(max_length=32,blank=True,null=True)

    player11_resault=models.CharField(max_length=12,blank=True,null=True)
    player11_name=models.CharField(max_length=32,blank=True,null=True)
    player11_hero=models.CharField(max_length=32,blank=True,null=True)
    player11_kills=models.IntegerField(blank=True,null=True)
    player11_dies=models.IntegerField(blank=True,null=True)
    player11_helps=models.IntegerField(blank=True,null=True)
    player11_wins=models.CharField(max_length=12,blank=True,null=True)
    player11_soldiers=models.IntegerField(blank=True,null=True)
    player11_golds=models.IntegerField(blank=True,null=True)
    player11_skill1=models.CharField(max_length=12,blank=True,null=True)
    player11_skill2=models.CharField(max_length=12,blank=True,null=True)
    player11_item1=models.CharField(max_length=64,blank=True,null=True)
    player11_item2=models.CharField(max_length=64,blank=True,null=True)
    player11_item3=models.CharField(max_length=64,blank=True,null=True)
    player11_item4=models.CharField(max_length=64,blank=True,null=True)
    player11_item5=models.CharField(max_length=64,blank=True,null=True)
    player11_item6=models.CharField(max_length=64,blank=True,null=True)
    player11_gain_golds=models.IntegerField(blank=True,null=True)
    player11_gain_exp=models.IntegerField(blank=True,null=True)
    player11_jiecao=models.BigIntegerField(blank=True,null=True)
    player11_win_p=models.CharField(max_length=32,blank=True,null=True)

    player12_resault=models.CharField(max_length=12,blank=True,null=True)
    player12_name=models.CharField(max_length=32,blank=True,null=True)
    player12_hero=models.CharField(max_length=32,blank=True,null=True)
    player12_kills=models.IntegerField(blank=True,null=True)
    player12_dies=models.IntegerField(blank=True,null=True)
    player12_helps=models.IntegerField(blank=True,null=True)
    player12_wins=models.CharField(max_length=12,blank=True,null=True)
    player12_soldiers=models.IntegerField(blank=True,null=True)
    player12_golds=models.IntegerField(blank=True,null=True)
    player12_skill1=models.CharField(max_length=12,blank=True,null=True)
    player12_skill2=models.CharField(max_length=12,blank=True,null=True)
    player12_item1=models.CharField(max_length=64,blank=True,null=True)
    player12_item2=models.CharField(max_length=64,blank=True,null=True)
    player12_item3=models.CharField(max_length=64,blank=True,null=True)
    player12_item4=models.CharField(max_length=64,blank=True,null=True)
    player12_item5=models.CharField(max_length=64,blank=True,null=True)
    player12_item6=models.CharField(max_length=64,blank=True,null=True)
    player12_gain_golds=models.IntegerField(blank=True,null=True)
    player12_gain_exp=models.IntegerField(blank=True,null=True)
    player12_jiecao=models.BigIntegerField(blank=True,null=True)
    player12_win_p=models.CharField(max_length=32,blank=True,null=True)

    player13_resault=models.CharField(max_length=12,blank=True,null=True)
    player13_name=models.CharField(max_length=32,blank=True,null=True)
    player13_hero=models.CharField(max_length=32,blank=True,null=True)
    player13_kills=models.IntegerField(blank=True,null=True)
    player13_dies=models.IntegerField(blank=True,null=True)
    player13_helps=models.IntegerField(blank=True,null=True)
    player13_wins=models.CharField(max_length=12,blank=True,null=True)
    player13_soldiers=models.IntegerField(blank=True,null=True)
    player13_golds=models.IntegerField(blank=True,null=True)
    player13_skill1=models.CharField(max_length=12,blank=True,null=True)
    player13_skill2=models.CharField(max_length=12,blank=True,null=True)
    player13_item1=models.CharField(max_length=64,blank=True,null=True)
    player13_item2=models.CharField(max_length=64,blank=True,null=True)
    player13_item3=models.CharField(max_length=64,blank=True,null=True)
    player13_item4=models.CharField(max_length=64,blank=True,null=True)
    player13_item5=models.CharField(max_length=64,blank=True,null=True)
    player13_item6=models.CharField(max_length=64,blank=True,null=True)
    player13_gain_golds=models.IntegerField(blank=True,null=True)
    player13_gain_exp=models.IntegerField(blank=True,null=True)
    player13_jiecao=models.BigIntegerField(blank=True,null=True)
    player13_win_p=models.CharField(max_length=32,blank=True,null=True)

    player14_resault=models.CharField(max_length=12,blank=True,null=True)
    player14_name=models.CharField(max_length=32,blank=True,null=True)
    player14_hero=models.CharField(max_length=32,blank=True,null=True)
    player14_kills=models.IntegerField(blank=True,null=True)
    player14_dies=models.IntegerField(blank=True,null=True)
    player14_helps=models.IntegerField(blank=True,null=True)
    player14_wins=models.CharField(max_length=12,blank=True,null=True)
    player14_soldiers=models.IntegerField(blank=True,null=True)
    player14_golds=models.IntegerField(blank=True,null=True)
    player14_skill1=models.CharField(max_length=12,blank=True,null=True)
    player14_skill2=models.CharField(max_length=12,blank=True,null=True)
    player14_item1=models.CharField(max_length=64,blank=True,null=True)
    player14_item2=models.CharField(max_length=64,blank=True,null=True)
    player14_item3=models.CharField(max_length=64,blank=True,null=True)
    player14_item4=models.CharField(max_length=64,blank=True,null=True)
    player14_item5=models.CharField(max_length=64,blank=True,null=True)
    player14_item6=models.CharField(max_length=64,blank=True,null=True)
    player14_gain_golds=models.IntegerField(blank=True,null=True)
    player14_gain_exp=models.IntegerField(blank=True,null=True)
    player14_jiecao=models.BigIntegerField(blank=True,null=True)
    player14_win_p=models.CharField(max_length=32,blank=True,null=True)

    player1_user_lv=models.IntegerField(blank=True,null=True)
    player1_hero_lv=models.IntegerField(blank=True,null=True)
    player2_user_lv=models.IntegerField(blank=True,null=True)
    player2_hero_lv=models.IntegerField(blank=True,null=True)
    player3_user_lv=models.IntegerField(blank=True,null=True)
    player3_hero_lv=models.IntegerField(blank=True,null=True)
    player4_user_lv=models.IntegerField(blank=True,null=True)
    player4_hero_lv=models.IntegerField(blank=True,null=True)
    player5_user_lv=models.IntegerField(blank=True,null=True)
    player5_hero_lv=models.IntegerField(blank=True,null=True)
    player6_user_lv=models.IntegerField(blank=True,null=True)
    player6_hero_lv=models.IntegerField(blank=True,null=True)
    player7_user_lv=models.IntegerField(blank=True,null=True)
    player7_hero_lv=models.IntegerField(blank=True,null=True)
    player8_user_lv=models.IntegerField(blank=True,null=True)
    player8_hero_lv=models.IntegerField(blank=True,null=True)
    player9_user_lv=models.IntegerField(blank=True,null=True)
    player9_hero_lv=models.IntegerField(blank=True,null=True)
    player10_user_lv=models.IntegerField(blank=True,null=True)
    player10_hero_lv=models.IntegerField(blank=True,null=True)
    player11_user_lv=models.IntegerField(blank=True,null=True)
    player11_hero_lv=models.IntegerField(blank=True,null=True)
    player12_user_lv=models.IntegerField(blank=True,null=True)
    player12_hero_lv=models.IntegerField(blank=True,null=True)
    player13_user_lv=models.IntegerField(blank=True,null=True)
    player13_hero_lv=models.IntegerField(blank=True,null=True)
    player14_user_lv=models.IntegerField(blank=True,null=True)
    player14_hero_lv=models.IntegerField(blank=True,null=True)
