###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("fall")

q1 = codesters.Square (100, 100, 200, 'MidnightBlue')
q2 = codesters.Square (-100, 100, 200, 'PowderBlue')
q3 = codesters.Square (-100, -100, 200, 'MidnightBlue')
q4 = codesters.Square (100, -100, 200, 'PowderBlue')

s1 = codesters.Sprite ("flower", 100, 100)
s1.set_size(3)
s2 = codesters.Sprite ("applecore", -100, -100)
s2.set_size(1.5)
s3 = codesters.Sprite ("sunshine", 100, -100)
s3.set_size(0.21)
s4 = codesters.Sprite ("coralinesquid", -100, 100)
s4.set_size(0.35)

message1 = codesters.Text ("Fiona Parviz",0,220,"black")
message2 = codesters.Text ("I thought it was a bird but it was just a paper bag",0,-220,"black")