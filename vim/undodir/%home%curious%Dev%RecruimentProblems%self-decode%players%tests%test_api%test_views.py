Vim�UnDo� U�^NDt~C�j���e�0�)^]$L�)S���   c   Z        # can't use a fake name from the faker because apparently names aren't allowed '.'      W      &       &   &   &    `��U    _�                             ����    "                                                                                                                                                                                                                                                                                                                                                        `��    �         d       �         c    5�_�                           ����    #                                                                                                                                                                                                                                                                                                                                                        `��     �                        breakpoint()5�_�                           ����    "                                                                                                                                                                                                                                                                                                                                                        `��    �         d       �         c    5�_�                   <       ����    #                                                                                                                                                                                                                                                                                                                                                        `��     �   ;   =   e       �   ;   =   d    5�_�                    <       ����    #                                                                                                                                                                                                                                                                                                                                                        `��     �   <   >   f       �   <   >   e    5�_�      	             =       ����    #                                                                                                                                                                                                                                                                                                                                                        `��'     �   <   =                  name = faker.name()5�_�      
           	   <       ����    #                                                                                                                                                                                                                                                                                                                                                        `��(     �   ;   =   e    �   <   =   e    5�_�   	              
   >   F    ����    #                                                                                                                                                                                                                                                                                                                                                        `��H     �   =   ?   f      T        response = client.post(self.url, {'team_id': team.id, 'name': faker.name()})5�_�   
                 >   F    ����    #                                                                                                                                                                                                                                                                                                                                                        `��I     �   =   ?   f      O        response = client.post(self.url, {'team_id': team.id, 'name': .name()})5�_�                    >   F    ����    #                                                                                                                                                                                                                                                                                                                                                        `��J     �   =   ?   f      N        response = client.post(self.url, {'team_id': team.id, 'name': name()})5�_�                   >   F    ����    #                                                                                                                                                                                                                                                                                                                                                        `��]     �   =   ?   f      J        response = client.post(self.url, {'team_id': team.id, 'name': ()})5�_�                    >   J    ����    #                                                                                                                                                                                                                                                                                                                                                        `��c     �   =   ?   f      N        response = client.post(self.url, {'team_id': team.id, 'name': name()})5�_�                    >   J    ����    #                                                                                                                                                                                                                                                                                                                                                        `��d    �   =   ?   f      M        response = client.post(self.url, {'team_id': team.id, 'name': name)})5�_�                           ����    #                                                                                                                                                                                                                                                                                                                                                        `��8     �         g           �         g       �         f    5�_�                            ����    #                                                                                                                                                                                                                                                                                                                                                        `��F     �                        breakpoint()5�_�                       K    ����    "                                                                                                                                                                                                                                                                                                                                                        `��Q     �         e      Q        response = client.post(self.url, data={'team_id': team_id, 'name': name})5�_�                           ����    "                                                                                                                                                                                                                                                                                                                                                        `��V     �                        name = faker.name()5�_�                           ����    !                                                                                                                                                                                                                                                                                                                                                        `��X     �         e       �         d    5�_�                    <       ����    "                                                                                                                                                                                                                                                                                                                                                        `��     �   ;   <                  breakpoint()5�_�                    ;       ����    "                                                                                                                                                                                                                                                                                                                                                        `��     �   :   ;                  name = faker.name()5�_�                    ;   F    ����    "                                                                                                                                                                                                                                                                                                                                                        `��     �   :   <   c      L        response = client.post(self.url, {'team_id': team.id, 'name': name})5�_�                       B    ����    "                                                                                                                                                                                                                                                                                                                                                        `��     �         c      J    def test_valid_name_and_team_id(self, client, team, team_data, faker):5�_�                       B    ����    "                                                                                                                                                                                                                                                                                                                                                        `��     �         c      I    def test_valid_name_and_team_id(self, client, team, team_data,faker):5�_�                       A    ����    "                                                                                                                                                                                                                                                                                                                                                        `��     �         c      D    def test_valid_name_and_team_id(self, client, team, team_data,):5�_�                    4   Z    ����    "                                                                                                                                                                                                                                                                                                                                                        `���     �   3   5   c      b    def test_creating_a_player_after_15_players_in_a_team(self, team, monkeypatch, client, faker):5�_�                     4   Z    ����    "                                                                                                                                                                                                                                                                                                                                                        `���     �   3   5   c      a    def test_creating_a_player_after_15_players_in_a_team(self, team, monkeypatch, client,faker):5�_�      !              4   Y    ����    "                                                                                                                                                                                                                                                                                                                                                        `���    �   3   5   c      \    def test_creating_a_player_after_15_players_in_a_team(self, team, monkeypatch, client,):5�_�       "           !   "       ����    "                                                                                                                                                                                                                                                                                                                                                        `���    �   !   #   c                      'name': name,5�_�   !   #           "   "       ����    "                                                                                                                                                                                                                                                                                                                                                        `��c     �   !   #   c                      'name': 'a',5�_�   "   $           #      L    ����    "                                                                                                                                                                                                                                                                                                                                                        `��|     �         c      P        response = client.post(self.url, data={'team_id': team_id, 'name': 'a'})5�_�   #   %           $   ;   G    ����    "                                                                                                                                                                                                                                                                                                                                                        `��    �   :   <   c      K        response = client.post(self.url, {'team_id': team.id, 'name': 'a'})5�_�   $   &           %      L    ����    "                                                                                                                                                                                                                                                                                                                                                        `��    �         c      S        response = client.post(self.url, data={'team_id': team_id, 'name': 'home'})5�_�   %               &      W    ����    "                                                                                                                                                                                                                                                                                                                                                        `��T    �         c      Z        # can't use a fake name from the faker because apparently names aren't allowed '.'5�_�                     4   Y    ����    "                                                                                                                                                                                                                                                                                                                                                        `���     �   3   5   c      Y    def test_creating_a_player_after_15_players_in_a_team(self, team, monkeypatch, client5�_�                   >   F    ����    #                                                                                                                                                                                                                                                                                                                                                        `��M     �   =   ?   f      F        response = client.post(self.url, {'team_id': team.id, 'name': 5�_�                     T   	    ����    #                                                                                                                                                                                                                                                                                                                                                        `��Q     �   S   U   f              gmeame_1 = GameFactory(5�_�                    >       ����    #                                                                                                                                                                                                                                                                                                                                                        `��"     �   =   ?   f      Q        response = client.u(self.url, {'team_id': team.id, 'name': faker.name()})5�_�                    >       ����    #                                                                                                                                                                                                                                                                                                                                                        `���     �   =   >   d       5��