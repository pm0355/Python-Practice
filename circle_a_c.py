
#/**********************************************************************/
#/* CSC 280 – Programming Project 1 */
#/* */
#/* modifier: Paul Mattioli*/
#/* */
#/* filename: circle_a_c.py
#/* */
#/* action: computes the area and circumference of a rectangle. */
#/* */
#/* input: the rectangle's length and then its width, entered by the */
#/* user as prompted for, and given as real numbers. */
#/* */
#/* output: the rectangle's area and circumference are output to the */
#/* screen, also as real numbers. */
#/* */
#/**********************************************************************/

radius = float(raw_input(" What is the radius of the circle? "))
pi = 3.14
diameter = 2 * radius
circumference = float(pi) * float(diameter)
area = pi * radius * radius
print " Circumference = " + str(circumference)
print " Area = " + str(area)


