# Put You On (PYO)

## A Music Sharing Platform to Connect with Others

PYO is a unique social network that focuses on music sharing rather than traditional photo or video sharing. It allows users to connect with each other based on their music taste and preferences. The app features a card-based UI, where users can view and interact with different music-related posts.
The app's main feature is the ability for users to respond to premade prompts with four songs. These prompts can range from simple questions like "What song makes you happy?" to more nostalgic ones like "What song takes you back to your childhood?" Users can choose any four songs they like and share them with the community.
Other users can then upvote or downvote the posts based on their personal preferences. They can also leave comments, which create a discussion board-like environment where users can engage with each other and share their thoughts on the songs. They can also filter through posts based on genre.
In addition to providing a platform for music lovers to connect, PYO can also be a valuable tool for music producers. By researching the trending posts, producers can gain insights into the type of music that's currently popular and create music that resonates with the app's user base.

## User Personas

This project was created with three different user personas for Playtopia in mind:
1. Casual User
2. Music Artist
3. Music Curator

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## Project Creators

The 4 members of "Cupid Shuffle" are the students of Dr. Fontenot's CS3200 class below:

1. Aiden Jolibois - jolibois.a@northeastern.edu
2. Kelsey Nihezagirwe - nihezagirwe.k@northeastern.edu
3. Surya Ramakrishnan - ramakrishnan.sur@northeastern.edu
4. Toluwani Adelani - adelani.t@northeastern.edu


