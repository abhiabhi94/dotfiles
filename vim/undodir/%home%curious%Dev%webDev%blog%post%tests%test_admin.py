Vim�UnDo� \8k_E�t�Ɛ��M��l�^���fJL���                     '       '   '   '    `��A    _�                             ����                                                                                                                                                                                                                                                                                                                                                             `���     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��      �                 �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��     �                 class TestPostAdmin5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��<     �                  �               5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                             `��h     �         	       �             5�_�                       &    ����                                                                                                                                                                                                                                                                                                                                                             `��     �         	      +        url = self.admin.view_on_site(post)5�_�                       4    ����                                                                                                                                                                                                                                                                                                                                                             `��     �         
       �         	    5�_�      	                 .    ����                                                                                                                                                                                                                                                                                                                                                             `��     �                �             5�_�                 	      ,    ����                                                                                                                                                                                                                                                                                                                                                             `��     �               6        url = self.admin.view_on_site(self.draft_post)5�_�   	      
                 ����                                                                                                                                                                                                                                                                                                                                                             `��     �                       �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `��     �                       @staticmethod5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `��     �                    def setUp(self):5�_�                          ����                                                                                                                                                                                                                                                                                                                                                v       `��C     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `��G     �                 �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `��_     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `��k     �               @        cls.model_admin = FlaggedContentAdmin(Flag, AdminSite())5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                v       `��p     �               6        cls.model_admin = PostAdmin(Flag, AdminSite())5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `��t     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `��     �                �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `���     �                ;        self.assertEqual(url, draft_post.get_preview_url())5�_�                        "    ����                                                                                                                                                                                                                                                                                                                                                v       `���     �      !   !       �      !        5�_�                    !       ����                                                                                                                                                                                                                                                                                                                                                v       `��     �                  4    def test_view_on_site_with_debug_disabled(self):5�_�                    !   &    ����                                                                                                                                                                                                                                                                                                                                                v       `��     �   !               �   !            5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       `��c    �                     �                        5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `���    �         $      'from post.test.base import TestPostBase5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       `���    �         %       �         $    5�_�                           ����                                                                                                                                                                                                                                                                                                                            	          	          v       `��    �         %      6        url = self.admin.view_on_site(self.draft_post)5�_�                    	       ����                                                                                                                                                                                                                                                                                                                            	                           `��    �   	      %          def _mock_request(user):           class MockRequest:               pass               request = MockRequest()           request.user = user           return request�      
   %          @staticmethod5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                      %          v       `���     �              
   3    def test_view_on_site_for_published_post(self):   6        url = self.model_admin.view_on_site(self.post)       :        self.assertEqual(url, self.post.get_preview_url())       "    @override_settings(DEBUG=True)   .    def test_view_on_site_in_debug_mode(self):   6        url = self.model_admin.view_on_site(self.post)       :        self.assertEqual(url, self.post.get_preview_url())5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                v       `���     �                9       self.assertEqual(url, self.post.get_preview_url())5�_�   !   #           "   	        ����                                                                                                                                                                                                                                                                                                                            	                      v        `���     �      
      
       #@staticmethod       #def _mock_request(user):       #    class MockRequest:       #        pass            #    request = MockRequest()       #    request.user = user       #    return request           @classmethod5�_�   "   &           #           ����                                                                                                                                                                                                                                                                                                                            	           	           v        `���    �                )from django.test import override_settings5�_�   #   '   %       &           ����                                                                                                                                                                                                                                                                                                                                                  v        `��>     �                  *from django.contrib.admin import AdminSite       (from post.tests.base import TestPostBase    from post.admin import PostAdmin   from post.models import Post       "class TestPostAdmin(TestPostBase):       @classmethod       def setUpTestData(cls):           super().setUpTestData()   6        cls.model_admin = PostAdmin(Post, AdminSite())       /    def test_view_on_site_for_draft_post(self):   <        url = self.model_admin.view_on_site(self.draft_post)       @        self.assertEqual(url, self.draft_post.get_preview_url())    5�_�   &               '           ����                                                                                                                                                                                                                                                                                                                                                  v        `��@    �             5�_�   #       $   &   %           ����                                                                                                                                                                                                                                                                                                                            	           	           v        `��7     �                5�_�   #           %   $           ����                                                                                                                                                                                                                                                                                                                            	           	           v        `��5     �                5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            	                     v       `��     �      
   %      j    @staticmethod5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                v       `��     �   	           5�_�   	              
      +    ����                                                                                                                                                                                                                                                                                                                                                             `��     �             �               8    def test_view_on_site_for_draft_post(se@staticmethod       def _mock_request(user):           class MockRequest:               pass               request = MockRequest()           request.user = user           return request           @classmethod       def setUpTestData(cls):           super().setUpTestData()   D        cls.model_admin = FlaggedContentAdmin(Flag, AdminSite())lf):5��