import movie
import actor
import fresh_tomatoes

###########################
# Movies :
###########################

wolf = movie.Movie( "Wolf of Wall Street",
                    "http://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                    "www.youtube.com/watch?v=iszwuX1AK6A" )

pulp = movie.Movie( "Pulp Fiction",
                    "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                    "www.youtube.com/watch?v=s7EdQ4FqbhY" )

gatsby = movie.Movie( "Great Gatsby",
                      "http://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
                      "www.youtube.com/watch?v=8ud6haTTfFY" )

vacation =  movie.Movie( "National Lampoon's Christmas Vacation",
                         "http://upload.wikimedia.org/wikipedia/en/5/53/NationalLampoonsChristmasVacationPoster.JPG",
                         "www.youtube.com/watch?v=NBTTipJX-h4" )

dumb = movie.Movie( "Dumb & Dumber",
                    "http://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
                    "www.youtube.com/watch?v=2fvoau0ekWk" )

###########################
# Actors :
###########################
leonardo = actor.Actor( "Leonardo Dicaprio",
                        "https://pbs.twimg.com/profile_images/344513261567840137/c253a2c039a701b65d5b2e92fc1735cc_normal.jpeg",
                        "http://en.wikipedia.org/wiki/Leonardo_DiCaprio" )

duchess = actor.Actor ( "Margot Robbie",
                        "https://pbs.twimg.com/profile_images/425523950341218305/DSrCtA3Y_normal.jpeg",
                        "http://en.wikipedia.org/wiki/Margot_Robbie" )

donnie = actor.Actor( "Jonah Hill",
                      "https://gp3.googleusercontent.com/-IezDMxxplG8/AAAAAAAAAAI/AAAAAAAAAB8/Tr6-JLpNISE/s48-c-k-no/photo.jpg",
                      "http://en.wikipedia.org/wiki/Jonah_Hill" )


travolta = actor.Actor( "John Travolta",
                        "https://gp3.googleusercontent.com/-OgFiKlkXz48/AAAAAAAAAAI/AAAAAAAAACg/JCLtS6y72NQ/s48-c-k-no/photo.jpg",
                        "http://en.wikipedia.org/wiki/John_Travolta")               
                        
jackson = actor.Actor( "Samuel L. Jackson",
                       "http://cdn8.staztic.com/app/a/765/765108/pulp-fiction-ezekiel-2517-253542-l-48x48.png",
                       "http://en.wikipedia.org/wiki/Samuel_L._Jackson")
                       
uma = actor.Actor( "Uma Thurman",
                   "https://pbs.twimg.com/profile_images/1808159711/umat_normal.jpg",
                   "http://en.wikipedia.org/wiki/Uma_Thurman" )
                   

# Add actors to movies
wolf.add_actor( leonardo )
wolf.add_actor( duchess )
wolf.add_actor( donnie )

pulp.add_actor( travolta )
pulp.add_actor( jackson )
pulp.add_actor( uma )




###########################
# Play :
###########################
my_movies = [ wolf, pulp, gatsby, vacation, dumb ]


fresh_tomatoes.open_movies_page( my_movies )

                            
