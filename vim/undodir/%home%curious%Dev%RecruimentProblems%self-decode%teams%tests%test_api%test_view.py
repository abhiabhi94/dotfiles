Vim�UnDo� �Y�G�t,��0�b�rF:�g�:�=Y�B���   !                 =       =   =   =    `�}�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             `�xZ     �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�xo     �                k5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�xo     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�xp     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�x�     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�x�     �         	    5�_�      	             
        ����                                                                                                                                                                                                                                                                                                                                                             `�y
     �   	                  �   
            5�_�      
           	   
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y     �   	            0 team_1 = TeamFactory.create(name='test-team-1')5�_�   	              
   
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y     �   	            4     team_1 = TeamFactory.create(name='test-team-1')5�_�   
                 
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y     �   	            8         team_1 = TeamFactory.create(name='test-team-1')5�_�                   
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y     �   	            7        team_1 = TeamFactory.create(name='test-team-1')5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y     �   	   
                  5�_�                            ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y%     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y5     �                       assert game5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�yV     �                .        assert Game.objects.all().count() == 35�_�                            ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�yW     �                 5�_�                    	   >    ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�yb     �      
         @    def test_get_request_is_ordered_by_wins(self, game, team_1):5�_�                           ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y�     �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y�     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `�y�     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y�     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `�y�     �                �             5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                v       `�z     �               [        assert response.json() == [team_data(team_1), team_data(team_2), team_data(team_3))5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `�z     �               8team_data(team_1), team_data(team_2), team_data(team_3))5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                v       `�z     �               H                team_data(team_1), team_data(team_2), team_data(team_3))5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                v       `�z     �               5                team_data(team_2), team_data(team_3))5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                v       `�z     �               4                team_data(team_2),team_data(team_3))5�_�                       "    ����                                                                                                                                                                                                                                                                                                                                                v       `�z(     �                "                team_data(team_3))5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `�z2     �                :        assert list(Team.objects.get_teams_by_wins()) == [5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                v       `�z3     �                !                team_1,  # 2 wins5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                v       `�z4     �                                 team_2,  # 1 win5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                v       `�z4     �                                team,  # 0 wins5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                v       `�z5     �                            ]5�_�   #   %           $      "    ����                                                                                                                                                                                                                                                                                                                                                v       `�z7     �               "                team_data(team_1),5�_�   $   &           %      "    ����                                                                                                                                                                                                                                                                                                                                                v       `�z>     �               "                team_data(team_2),5�_�   %   '           &      "    ����                                                                                                                                                                                                                                                                                                                                                v       `�zI     �               "                team_data(team_3),5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                v       `�zQ    �                   �                        5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                v       `�z�    �                   url = reverse('games:list')5�_�   (   *           )   
   I    ����                                                                                                                                                                                                                                                                                                                                                v       `�|     �   	            K    def test_get_request_is_ordered_by_wins(self, game, team_1, team_data):5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                                                v       `�|$     �               ,        response = self.client.get(self.url)5�_�   *   ,           +          ����                                                                                                                                                                                                                                                                                                                                                v       `�|&    �               (        response = .client.get(self.url)5�_�   +   -           ,   
   <    ����                                                                                                                                                                                                                                                                                                                                                v       `�|�     �   	            S    def test_get_request_is_ordered_by_wins(self, game, team_1, team_data, client):5�_�   ,   .           -   
   <    ����                                                                                                                                                                                                                                                                                                                                                v       `�|�    �   	            R    def test_get_request_is_ordered_by_wins(self, game, team1, team_data, client):5�_�   -   /           .           ����                                                                                                                                                                                                                                                                                                                                                v       `�|�    �                �             5�_�   .   0           /           ����                                                                                                                                                                                                                                                                                                                                                v       `�|�    �               'from teams.factories import TeamFactory    �                    �                �             5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                v       `�|�     �               ,                team_data(team_3),  # 0 wins5�_�   0   2           1          ����                                                                                                                                                                                                                                                                                                                                                v       `�|�    �               +                team_data(team3),  # 0 wins5�_�   1   3           2      O    ����                                                                                                                                                                                                                                                                                                                                                v       `�}N     �               Q    def test_get_request_is_ordered_by_wins(self, game, team, team_data, client):5�_�   2   4           3      8    ����                                                                                                                                                                                                                                                                                                                                                v       `�}]    �                 �             5�_�   3   5           4      (    ����                                                                                                                                                                                                                                                                                                                                                v       `�}z   	 �                -        assert django_assert_num_queries == 15�_�   4   6           5      )    ����                                                                                                                                                                                                                                                                                                                                                v       `�}�     �                /        assert django_assert_num_queries() == 15�_�   5   7           6      +    ����                                                                                                                                                                                                                                                                                                                                                v       `�}�   
 �                0        assert django_assert_num_queries(1) == 15�_�   6   8           7      +    ����                                                                                                                                                                                                                                                                                                                                                v       `�}�     �                +        assert django_assert_num_queries(1)5�_�   7   :           8      -    ����                                                                                                                                                                                                                                                                                                                                                v       `�}�     �                y        assert django_assert_num_queries(1)  # optimizing this was one of the requirements mentioned in the test document5�_�   8   ;   9       :      *    ����                                                                                                                                                                                                                                                                                                                                                v       `�}�     �              5�_�   :   <           ;           ����                                                                                                                                                                                                                                                                                                                                                v       `�}�     �         !       �         !    5�_�   ;   =           <      K    ����                                                                                                                                                                                                                                                                                                                               K          K       v   K    `�}�     �         !      L# optimizing this was one of the requirements mentioned in the test document5�_�   <               =          ����                                                                                                                                                                                                                                                                                                                                                v       `�}�    �         !      P    # optimizing this was one of the requirements mentioned in the test document5�_�   8           :   9      *    ����                                                                                                                                                                                                                                                                                                                                                v       `�}�     �              �                w        assert django_assert_num_queries(1# optimizing this was one of the requirements mentioned in the test document)5�_�                    
       ����                                                                                                                                                                                                                                                                                                                            
          
          v       `�y     �   	            8        uteam_1 = TeamFactory.create(name='test-team-1')5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             `�x�     �   	   
   
       �   	                    team_   5��