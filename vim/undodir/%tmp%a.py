Vim�UnDo� �5��U�O(��R�Dm�L�^�J���)��                    +       +   +   +    `���    _�                             ����                                                                                                                                                                                                                                                                                                                                                             `�I:     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�IU     �                 �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�If    �               
    a: int5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�I�    �               class B:5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�J     �                from typing import List5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�J     �                   a: List[int]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�J    �                   a: ClassVar[List[int]5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             `�PF   
 �                   a: ClassVar[List[int]]5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             `��     �      	   	       �      	       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `���     �      	   	          print(reveal_type(A))5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��     �                    print(reveal_type(B.a))5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��    �      	   	       �      	       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��7    �         	           a: ClassVar[List[int]] = ...5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��H     �         	          a: ClassVar[List[int]] 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��L     �         	          a: ClassVar[List[int] 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��M    �         	          a: ClassVarList[int] 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `��p    �      
   
       �      
   	    5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             `���    �   	             �   	      
    5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             `���     �   	   
              reveal_globals()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `���    �         
          a: List[int] 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `���     �                    a: List[int] = [1]5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             `���     �         	    5�_�      !                       ����                                                                                                                                                                                                                                                                                                                                                             `���    �         
       5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `��)     �         
          a: ...  # type: List[int]5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `��-    �         
          a= ...  # type: List[int]5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `���    �                 �          
    5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `��b     �                 "from __future__ import annotations5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `��c     �                  5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `��l     �         
          a = ...  # type: List[int]5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `��y     �         
      )    a: List[int[ = ...  # type: List[int]5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `���     �         
      )    a: List[int] = ...  # type: List[int]5�_�   (   +           )          ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `���    �         
          a: List[int5�_�   )       *       +      
    ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `���    �                �         
    5�_�   )           +   *      
    ����                                                                                                                                                                                                                                                                                                                               
          
       v   
    `���     �         
       5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             `�M1     �                �         	      #    def foo(self, a: int): -> None:           ...5�_�      
           	      
    ����                                                                                                                                                                                                                                                                                                                                                             `�MT     �      	   
       5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             `�MX    �                 �                       "    def foo(self, a: int) -> None:           return5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             `�M�    �               "    def foo(self, a: int) -> None:5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�M�     �               !    def foo(self, a: int) -> int:5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�M�    �                        return 15�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�N    �                    a: ClassVar[List[int]] = [1]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             `�N0     �              5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             `�N1   	 �              5��