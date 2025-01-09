.. examples-section:

============
PDN Examples
============

All of the examples below have been checked with the `PDN 3.0 Checker <http://10x10.org/pdn/test/index.html>`_.

An example of an international draughts game in PDN 3.0 format:

::

  [Event "FMJD World Championship"]
  [Site "Hardenberg, NED"]
  [Date "2007.05.19"]
  [Round "7"]
  [White "Mikhalchenko,I."]
  [Black "Ndjofang,J."]
  [Result "0-2"]
  [GameType "20"]
  [WhiteTime "1:36"]
  [BlackTime "1:17"]
  
   1.32-28 17-22  2.28x17 11x22  3.37-32  6-11  4.41-37 12-17  5.46-41  8-12
   6.34-30  2-8   7.30-25 19-23  8.35-30  1-6   9.40-35 13-19 10.31-27 22x31
  11.36x27  9-13 12.33-28  4-9  13.41-36 17-22 14.28x17 11x31 15.37x26 23-28
  16.32x23 19x28 17.42-37 20-24 18.30x19 14x23 19.37-31 16-21 20.26x17 12x21
  21.31-27 21x32 22.38x27  6-11 23.47-42 15-20 24.25x14 10x19 25.39-33 28x39
  26.44x33  8-12 27.42-38 23-28 28.33x22 12-17 29.49-44 17x28 30.38-33 28x39
  31.44x33 18-22 32.27x18 13x22 33.43-38 19-23 34.38-32 11-17 35.32-27 22x31
  36.36x27  9-13 37.45-40 13-18 *

An example of an analysis in PDN 3.0 format:

::

  [Event "nk"]
  [Site "?"]
  [Date "2009.04.08"]
  [Round "?"]
  [White "Derkx,B."]
  [Black "Meijer,Hein"]
  [Result "2-0"]
  [GameType "20"]
  [WhiteTime "2.23"]
  [BlackTime "2.40"]
  [PlyCount "117"]
  
  { Beide spelers hebben volgens Turbo Dambase 3x eerder tegen elkaar
  gespeeld. In het Nederlands kampioenschap van 2007 en 2008, en in de
  halve finale van 2007, troffen beiden elkaar. Alle eerdere duels
  eindigde in remise. } 1. 34-29 17-22 2. 32-28 { Het populairste
  antwoord in deze opening is 2.39-34 op ruime afstand gevolgd door
  2.40-34 } 11-17 3. 37-32 6-11 4. 41-37 19-23 ( { Meestal wordt eerst
  } 4... 1-6 { gespeeld om na } 5. 46-41 { alsnog } 19-23 6. 28x19
  14x34 { te spelen. } ) 5. 28x19 14x34 6. 39x30 ( { Over het algemeen
  is slaan met } 6. 40x29 { populairder. } ) 6... 13-19 7. 44-39 8-13
  8. 50-44 20-25 9. 32-28 25x34 10. 40x29 16-21 11. 31-26 21-27
  12. 37-32 11-16 13. 32x21 16x27 14. 38-32 27x38 15. 43x32 10-14
  16. 49-43 5-10 17. 42-38 3-8 18. 47-42 19-23 19. 28x19 14x34
  20. 39x30 13-19 21. 43-39 10-14 22. 46-41 18-23 23. 41-37 12-18
  24. 37-31 7-12 25. 33-28 22x33 26. 39x28 15-20 27. 31-27 2-7
  28. 44-39 7-11 29. 39-33 20-24 30. 42-37 1-6 31. 48-42 9-13 32. 30-25
  23-29 33. 27-21 11-16 34. 37-31 16x27 35. 31x11 6x17 36. 45-40 17-21
  37. 26x17 12x21 38. 42-37 18-23 39. 36-31 21-26 40. 31-27 8-12
  41. 40-34 29x40 42. 35x44 4-10 43. 44-39 23-29 44. 28-22 13-18 ( {
  Zwart had hier } 44... 12-18 { moeten spelen } 45. 22-17 29-34
  46. 39x30 24x35 { enz. } ) 45. 22x13 19x8 46. 33-28 $1 8-13 47. 28-22
  13-19 $2 ( { In tijdnood gaat het nodige mis, aangewezen is hier }
  47... 10-15 48. 22-17 12x21 49. 27x16 13-19 { en ook zwart werkt aan
  zijn doorbraak. } ) 48. 25-20 $3 ( 48. 22-17 12x21 49. 27x16 26-31
  50. 37x26 24-30 51. 25x23 19x37 ) 48... 24x15 49. 22-17 12x21
  50. 27x16 15-20 51. 16-11 20-24 52. 11-7 29-34 53. 39x30 24x35
  54. 7-1 14-20 55. 32-27 20-24 56. 27-22 10-15 57. 1-45 24-30
  58. 22-17 19-24 59. 45-18 *
  
An example of a checkers game in PDN 3.0 format:

::

  [Event "Double Corner Dyke"]
  [Black "Jordan,A"]
  [White "Tesheliet,F"]
  [Event "This is an 8x8 draughts game"]
  [Result "1/2-1/2"]
  [GameType "21"]
  
  1.  9-14 22-17 2. 11-15 25-22 3. 15-19 {Forms the Double Corner Dyke, With
   black aiming to occupy sqr 19, attacking white's double corner.} 23x16 
  4. 12x19 24x15 5. 10x19 17x10 6.  6x15 21-17 7.  5-9 29-25 8.  8-12 25-21 
  9.  7-10 17-13 10.  1-6 {It seems unwise to abondon the key back row sqr 1,
   but it is necessary to prevent 13-9..} 27-24 11.  4-8 32-27 12.  9-14 
  27-23 13.  3-7 23x16 14. 12x19 22-17 15.  7-11 26-23 16. 19x26 30x23 
  17.  8-12 24-20 18. 15-18 23-19 19. 11-15 20-16 20. 15x24 28x19 21.  2-7 
  31-26 22. 18-23 26-22 23. 23-27 16-11 {! a really beautiful escape} 
  24.  7x23 22-18 *

An example of a live game captured with an electronic board, with clock times and two setups:

::

  [White "Player 1"]                                                                                                
  [Black "Player 2"]                                                                                                
  [Round "1"]                                                                                                       
  1.  32-28 {[%clock w0:00:00 B0:00:05]}                                                                            
      19-23 {[%clock W0:00:10 b0:00:15]}                                                                            
  2.  28x19 {[%clock w0:00:20 B0:00:25]}                                                                            
      14x23 {[%clock W0:00:30 b0:00:35]}                                                                            
  3.  34-29 {[%clock w0:00:40 B0:00:45]}                                                                            
      23x34 {[%clock W0:00:50 b0:00:55]}                                                                            
  4.  40x29 {[%clock w0:01:00 B0:01:05]}                                                                            
      10-14 {[%clock W0:01:10 b0:01:15]}                                                                            
  5.  37-32 {[%clock w0:01:20 B0:01:25]}                                                                            
      13-19 {[%clock W0:01:30 b0:01:35]}                                                                            
  6.  41-37 {[%clock w0:01:40 B0:01:45]}                                                                            
       8-13 {[%clock W0:01:50 b0:01:55]}                                                                            
  7.  46-41 {[%clock w0:02:00 B0:02:05]}                                                                            
       2-8  {[%clock W0:02:10 b0:02:15]}                                                                            
  8.  45-40 {[%clock w0:02:20 B0:02:25]}                                                                            
      17-21 {[%clock W0:02:30 b0:02:35]}                                                                            
  9.  31-26 {[%clock w0:02:40 B0:02:45]}                                                                            
      19-23 {[%clock W0:02:50 b0:02:55]}                                                                            
  10. 26x17 {[%clock w0:03:00 B0:03:05]}                                                                            
      23x45 {[%clock W0:03:10 b0:03:15]}                                                                            
  11. 36-31 {[%clock w0:03:20 B0:03:25]}                                                                            
      12x21 {[%clock W0:03:30 b0:03:35]}                                                                            
  12. 31-26 {[%clock w0:03:40 B0:03:45]}                                                                            
       7-12 {[%clock W0:03:50 b0:03:55]}                                                                            
  13. 26x17 {[%clock w0:04:00 B0:04:05]}                                                                            
      12x21 {[%clock W0:04:10 b0:04:15]}                                                                            
  14. 33-29 {[%clock w0:04:20 B0:04:25]}                                                                            
      21-26 {[%clock W0:04:30 b0:04:35]}                                                                            
  15. 41-36 {[%clock w0:04:40 B0:04:45]}                                                                            
      14-19 {[%clock W0:04:50 b0:04:55]}                                                                            
  16. 39-33 {[%clock w0:05:00 B0:05:05]}                                                                            
      20-24 {[%clock W0:05:10 b0:05:15]}                                                                            
  17. 29x20 {[%clock w0:05:20 B0:05:25]}                                                                            
      15x24 {[%clock W0:05:30 b0:05:35]}                                                                            
  /FEN "W:W32,33,35,36,37,38,42,43,44,47,48,49,50:B1,3,4,5,6,8,9,11,13,16,18,26,30,45"/ {[%clock W0:05:40 b0:05:45]}
  19. 35x24 {[%clock w0:05:50 B0:05:55]}                                                                            
  /FEN "W:W32,33,36,37,38,42,43,44,47,48,49,50:B1,3,4,5,6,8,9,11,13,16,18,26,30,45"/ {[%clock W0:06:00 b0:06:05]}   
  21. 32-28 {[%clock w0:06:10 B0:06:15]}                                                                            
      30-35 {[%clock W0:06:20 b0:06:25]}                                                                            
  22. 43-39 {[%clock w0:06:30 B0:06:35]}                                                                            
       1-7  {[%clock W0:06:40 b0:06:45]}                                                                            
  23. 37-32 {[%clock w0:06:50 B0:06:55]}                                                                            
       7-12 {[%clock W0:07:00 b0:07:05]}                                                                            
  24. 49-43 {[%clock w0:07:10 B0:07:15]}                                                                            
      18-22 {[%clock W0:07:20 b0:07:25]}                                                                            
  25. 28x17 {[%clock w0:07:30 B0:07:35]}                                                                            
      12x21 {[%clock W0:07:40 b0:07:45]}                                                                            
