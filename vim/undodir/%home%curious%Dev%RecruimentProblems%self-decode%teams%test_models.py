Vim�UnDo� �O�~��G<U+�D�޻��Yϭ�w4#���                                      `�P,    _�                            ����                                                                                                                                                                                                                                                                                                                                                             `�E�    �                   @pytest.mark.db5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�HM     �                 "        assert team == 'test-team'5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             `�HW     �                 '        assert team == 'Team test-team'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�H[    �                 +        assert str(team == 'Team test-team'5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �                   def test_str(self, team):5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �               %    def test_get_members(self, team):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �                 ,        assert str(team) == 'Team test-team'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �                 $        assert team.get_members() ==5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �                �             5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �      	       5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �                 )        assert list(team.get_members() ==5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�N�     �                '        members_qs = team.get_members()5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                                             `�O     �                 )        assert list(team.get_members() ==5�_�                       0    ����                                                                                                                                                                                                                                                                                                                                                             `�O    �                 0        assert list(team.get_members().all()) ==5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�O,    �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�O{    �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�P+    �                        breakpoint()5�_�         
                ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                -        assert str(team) == "'Team test-team'5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                .        assert str(team) == "'Team' test-team'5�_�                        $    ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                2        assert str(team) == "'Team' uuuutest-team'5�_�                
          ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                ,        assert str(team) == iTeam test-team'5�_�             
             ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                -        assert str(team) == '"Team test-team'5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                .        assert str(team) == '"Team" test-team'5�_�      	                 $    ����                                                                                                                                                                                                                                                                                                                                                             `�H�     �                /        assert str(team) == '"Team" "test-team'5�_�                  	      .    ����                                                                                                                                                                                                                                                                                                                                                             `�H�    �                0        assert str(team) == '"Team" "test-team"'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�HS     �                '        assert ueam == 'Team test-team'5��