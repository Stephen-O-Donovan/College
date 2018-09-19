<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
  <head>
    <meta http-equiv="Content-Type" 
          content="text/html; charset=iso-8859-1" />

    <title>CS2515 CA 01</title>
    <link type="text/css" rel="stylesheet" href="/~kb11/teaching/modules.css" />
  </head>

  <body>
  <div id="allcontent">
  <!-- the body of the page -->

    <p id="header">
      CS2515: Algorithms and Data Structures I
    </p>



    <div id="maincontent">
    <!-- the standard content of the page -->

      <!-- the text and other information -->
	  
      <h1>Continuous Assessment 1</h1>

      <p>
	    This lab is part of the formal continuous assessment for CS2515. It focuses on the implementation and use of the doubly linked list. It will count for up to 10% of the total marks available for CS2515.
	  </p>
	  
	  <p>
	    Since this is part of the formal assessment, the University's rules on plagiarism apply. You should not copy
		anyone else's code, you should not download code obtained from any website, and you should not get anybody
		else to write the code for you. The work you submit must be your own. However, you are free to reuse any code
		that has been delivered this year in CS2515 lectures or labs.
	  </p>
	  
	  <h2>The FlixNet Movie Library</h2>
	  
	  <ol>
	    <li> 
		  <p> Design and implement a class <code>Movie</code>, with fields <code>name</code>, <code>director</code>, 
		      <code>dateadded</code> and <code>viewed</code>(and you could have other fields for e.g. the cast list, 
			  the releasedate, the actual video file, the size of the file, the genre, etc, but we don't need them 
			  in this exercise). The dateadded field will contain 8 digit numbers in the form YYYYMMDD (technically, 
			  DD should not go above 31, MM above 12, and YYYY above 2017, but we will ignore that).
			  Your Movie class should
			  have an <code>__init__(...)</code> method, a <code>__str__()</code> method, a <code>get_title()</code>
			  method and a <code>play()</code> method to simulate the movie being played -- for this exercise, all it needs 
			  to do is ensure that <code>viewed</code> is set to True, and then return a string representation of 
			  the movie.
		  </p>
		</li>
		
		<li>
		  <p> Design and implement class <code>FlixNetLibrary</code>, which is essentially a sequence of movie objects. 
		      The library should offer the following methods (in addition to <code>__init__(...)</code>):
		    <ul>
			  <li><p><code>__str__()</code>, which should return the title of each movie in sequence in the string, indicating the current selected movie, if any</p></li>
			  <li><p><code>add_movie(movie)</code>, which should add a new movie to the library in decreasing order of dateadded</p></li>
			  <li><p><code>get_current()</code>, which should display the currently selected movie info</p></li>
			  <li><p><code>next_movie()</code>, which should change the current selection to the next one</p></li>
			  <li><p><code>prev_movie()</code>, which should change the current selection to the previous one</p></li>
			  <li><p><code>reset()</code>, which should reset the curent movie to the list head</p></li>
			  <li><p><code>play()</code>, which plays the currently selected movie - it should print a message saying the movie is being played, and should call the movie's own <code>play()</code> method</p></li>
			  <li><p><code>remove_current()</code>, which should remove the current movie from the library</p></li>
			  <li><p><code>length()</code>, which should report the number of movies in the library</p></li>
            </ul>
          </p>
        		  
          <p> The class <code>FlixNetLibrary</code> must be implemented as a doubly-linked list. You can create a separate 
		      Doubly-Linked List class, and then use an instance of that class as a field inside your FlixNetLibrary, or you can implement FlixNetLibrary to deal directly with a sequence of DLLNodes.
		  </p>
		  
		  <p> For this exercise, for invalid input, if we are obliged to return an item, we will return 
		      <code>None</code>, and otherwise we will do nothing. If you delete the currently selected movie, make whetever
			  came after it the new current selection; if that goes off the end of the list, reset the current movie to be the head.
		  </p>
		</li>
		
		<li><p>Test your class using the following sequence of operations:
		  <ol type=i>
		    <li>create an empty library</li>
			<li>create the movie ("Bladerunner 2049", "Villeneuve", 20171004, False) and add it to the library</li>
			<li>create the movie ("Hail, Caesar!", "Coen & Coen", 20160304, False) and add it to the library</li>
			<li>create the movie ("Wonder Woman", "Jenkins", 20170601, False) and add it to the library</li>
			<li>display the library to the screen</li>
			<li>set the current movies to be the next one (i.e. first in library)</li>
			<li>play the current movie</li>
			<li>move current to the next movie</li>
			<li>report the current movie</li>
			<li>move the current to the previous movie</li>
			<li>delete the current movie</li>
			<li>display the library to the screen</li>
			<li>create the movie ("The Imitation Game", "Tyldum", 20141114, False) and add it to the library</li>
			<li>move current to the next movie</li>
			<li>play the current movie</li>
			<li>display the library to the screen</li>
		  </ol>
		  <br/>
		  which should give you output something like:
		    <ul>
			<br/>
			---<br/>
			"Bladerunner 2049"<br/>
			"Wonder Woman"<br/>
			"Hail, Caesar!"<br/>
            <br/>
			---<br/>
			<br/>
			Currently playing: ("Bladerunner 2049", "Villeneuve", 20171004, True)<br/>
			<br/>
			Current movie: ("Wonder Woman", "Jenkins", 20170601, False)<br/>
			<br/>
			---<br/>
			>>>"Wonder Woman"<br/>
			"Hail, Caesar!"<br/>
   			<br/>
			---<br/>
			Currently playing: ("Hail, Caesar!", "Coen & Coen", 20160304, True)<br/>
			<br/>
			"Wonder Woman"<br/>
			>>>"Hail, Caesar!"<br/>
		    "The Imitation Game"<br/>
			---<br/>
			<br/>
			</ul>
          Note that you should also test using more extensive test methods than this. We will be using different methods to test your submitted software.
		</p></li>		

				 
		<li>
		  <p>Extend your design and implementation of the library to allow search for movies by substrings of the 
		     movie name or the director name. The methods should search the list from the current movie onwards, and
			 wrap around. If a matching movie is found, the current movie should be updated, and the method should
			 return <code>True</code>; if no movie is found, return <code>False</code>.
		  </p>
		</li>
	  </ol>


      <h3>Submission instructions</h3>

      <p>
        The submission deadline will be Friday 20th October, at 5pm.
		
		
		<ul>
		  <li>
		    <p>
			  You must submit a single file, which must be named <code>flixnet.py</code>. This file must contain your implementation of the Movie class, the FlixNetLibrary class, and the linked list classes.
			</p>
		  </li>
		  <li>
		    <p>
			  The file must not contain tabs - use spaces for the Python indentation. Make sure you test the implementation on the machines in the lab before submitting (and don't edit the files in any way after your last successful test)
			</p>
		  </li>
		  <li>
		    <p>
			  To submit, move into the directory containing your flixnet.py file, and type
			  <pre>
submit-ADS1 flixnet.py
              </pre>
			</p>
		  </li>
		  <li>
		    <p>
			  The submission system will be closed at 5pm on Friday 20th October.
			  Late submissions will not be accepted.
			</p>
		  </li>
		  <li>
		    <p>
			  Note that you can submit multiple times - only the final submission will be maintained by the system. 
			  In case you are rushing to meet the deadline, make sure you submit an early version in advance. 
			  This will also serve as a test that the submission system is working for you.
			</p>
		  </li>
		  <li>
		    <p>
			  Make sure that you compile and test your code before submitting, and that you submit exactly the version that you tested.
			</p>
		  </li>
		</ul>
      </p>		
			
			
		  
    </div>


    <p id="footer">
      <a href="/~kb11/teaching/CS2515/Home">CS2515</a> /
      <a href="/~kb11/">Ken Brown</a> /
      <a href="http://www.cs.ucc.ie">Computer Science</a> /
      <a href="http://www.ucc.ie">UCC</a>
    </p>

  </div>
  </body>
</html>



