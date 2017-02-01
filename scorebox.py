class Scorebox(object):
    """Creates a box score for NBA
    """

    def __init__(self, vTeam, vScore, hTeam, hScore, nugget):
        """Initialize a new Scorebox object.

        Args:
            vTeam (str): Visiting team's triCode
            vScore (str): Visiting team's score
            hTeam (str): Home team's triCode
            hScore (str): Home team's score
            nugget (str): Game nugget
        """

        self.vTeam = vTeam
        self.vScore = vScore
        self.hTeam = hTeam
        self.hScore = hScore
        self.nugget = nugget

        # set the total width of the box
        if len(self.nugget) == 0:
            self.totalwidth = 26
            self.nugget = u'\u2573' * self.totalwidth
        else:
            self.totalwidth = len(self.nugget)

        top = u'\u2554' + u'\u2550' * self.totalwidth + u'\u2557' + '\n'
        matchup = u'\u2551' + (self.vTeam + '@' + self.hTeam).rjust((self.totalwidth+7)/2) + u'\u2551'.rjust((self.totalwidth-3)/2) + '\n'
        visitor = u'\u2551' + self.vTeam + self.vScore.rjust(self.totalwidth - 3) + u'\u2551' + '\n'
        home = u'\u2551' + self.hTeam + self.hScore.rjust(self.totalwidth - 3) + u'\u2551' + '\n'
        divider = u'\u255f' + u'\u2500' * self.totalwidth + u'\u2562' + '\n'
        nugget = u'\u2551' + self.nugget + u'\u2551' + '\n'
        bottom = u'\u255a' + u'\u2550' * self.totalwidth + u'\u255d' + '\n'

        self.scorebox = top + matchup + visitor + home + divider + nugget + bottom
