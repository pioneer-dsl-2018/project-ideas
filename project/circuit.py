import SchemDraw
class circuit:

    #Constructors
    def __init__(self):
        # a list of lines. The line should be in order
        self.connection = []

    #connect lines in parallel
    def connectInParallel(self, *lines):
        for l in lines:
            self.connection.append(l)

    #connect lines in series
    def connectInSeries(self, *lines):
        for l in lines:
            self.connection.extend(l.elements)

    # There will be more methods to add a new line, or change the order of a line

    # mutators

    # this method converts the data to a valid SchemdDraw Program
    # 'RunAddress' is where Run.py is located; 'ImageName' is the filename of the generated image'
    def evaluate(self, ImageName):
                   SchemDraw.Drawing().add(SchemDraw.elements.LINE, d = 'right')
                   self.connection[0].evaluate()
                   SchemDraw.Drawing().draw()
                   SchemDraw.Drawing.save(ImageName)

