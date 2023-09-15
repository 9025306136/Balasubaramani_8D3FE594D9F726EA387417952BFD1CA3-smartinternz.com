class player:
  def play(self):
    print("the player is playing cricket ")
    class batsman:
      def play(self):
        print ("the batsman is batting")
        class bowler(player):
          def play(self):
            print("the bowler is bowling")
            
            p=player()
            
            p.play()
            
            p.play()
            