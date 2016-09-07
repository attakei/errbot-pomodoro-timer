Pomodoro timer
==============

.. image:: https://travis-ci.org/attakei/errbot-pomodoro-timer.svg?branch=master
   :target: https://travis-ci.org/attakei/errbot-pomodoro-timer


Support your life cycle with Pomdoro Technique.


What is Pomdoro Technique?
--------------------------

See `it <http://pomodorotechnique.com>`_


Installation
------------

.. code-block:: bash

   !repos install https://github.com/attakei/errbot-pomodoro-timer.git


Usage
-----

Turn on timer
^^^^^^^^^^^^^

.. code-block:: bash

   >>> !pomodoro start

On backend, timer counts 25 minutes for working and 5 minutes for resting..

..
   (wait 25 minutes..)
   Please rest for about 5 minutes
   (wait 5 minutes..)
   Let's work you about 25 minutes
   (loop infinite..)

Uuntil program had been stopped or be caught stop command, it run loop.

Turn off timer
^^^^^^^^^^^^^^

.. code-block:: bash

   >>> !pomodoro stop

