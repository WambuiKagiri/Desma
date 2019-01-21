/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Menu
4. Init Intro Slider
5. Init Price Slider
6. Init Google Map


******************************/

$(document).ready(function()
{
	"use strict";

	/* 

	1. Vars and Inits

	*/

	var header = $('.header');
	var menu = $('.menu');
	var menuActive = false;
	var ctrl = new ScrollMagic.Controller();
	var map;

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();

		setTimeout(function()
		{
			$(window).trigger('resize.px.parallax');
		}, 375);
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});

	initMenu();
	initIntroSlider();
	initPriceSlider();
	initGoogleMap();

	/* 

	2. Set Header

	*/

	function setHeader()
	{
		if($(window).scrollTop() > 127)
		{
			header.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
		}
	}

	/* 

	3. Init Menu

	*/

	function initMenu()
	{
		if($('.hamburger').length && $('.menu').length)
		{
			var hamb = $('.hamburger');
			var close = $('.menu_close_container');

			hamb.on('click', function()
			{
				if(!menuActive)
				{
					openMenu();
				}
				else
				{
					closeMenu();
				}
			});

			close.on('click', function()
			{
				if(!menuActive)
				{
					openMenu();
				}
				else
				{
					closeMenu();
				}
			});

	
		}
	}

	function openMenu()
	{
		menu.addClass('active');
		menuActive = true;
	}

	function closeMenu()
	{
		menu.removeClass('active');
		menuActive = false;
	}

	/* 

	4. Init Intro Slider

	*/

	function initIntroSlider()
	{
		if($('.intro_slider').length)
		{
			var introSlider = $('.intro_slider');
			introSlider.owlCarousel(
			{
				items:1,
				loop:true,
				autoplay:false,
				smartSpeed:1200,
				dots:false,
				nav:false
			});

			if($('.intro_slider_prev').length)
			{
				var prev = $('.intro_slider_prev');
				prev.on('click', function()
				{
					introSlider.trigger('prev.owl.carousel');
				});
			}

			if($('.intro_slider_next').length)
			{
				var next = $('.intro_slider_next');
				next.on('click', function()
				{
					introSlider.trigger('next.owl.carousel');
				});
			}
		}
	}

	/* 

	5. Init Price Slider

	*/

    function initPriceSlider()
    {
		$('input[type="range"]').rangeslider(
		{
			// Feature detection the default is `true`.
			// Set this to `false` if you want to use
			// the polyfill also in Browsers which support
			// the native <input type="range"> element.
			polyfill: false,

			// Default CSS classes
			rangeClass: 'rangeslider',
			disabledClass: 'rangeslider--disabled',
			horizontalClass: 'rangeslider--horizontal',
			verticalClass: 'rangeslider--vertical',
			fillClass: 'rangeslider__fill',
			handleClass: 'rangeslider__handle',

			// Callback function
			onInit: function() {},

			// Callback function
			onSlide: function(position, value) {},

			// Callback function
			onSlideEnd: function(position, value) {}
		});
    }

    /* 

	6. Init Google Map

	*/

	// function initGoogleMap()
	{
		var mymap = L.map('mapid').setView([-1.190179,36.932108], 13);
		
    	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={sk.eyJ1IjoiY2luZHlwcmlzY2lsbGEiLCJhIjoiY2pyMGw4M2doMDNwazN4cnB0a2NvbHAxcSJ9.tHgR1E8hjaf6aUF7jdwzYg}', {
    		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    		maxZoom: 18,
    		id: 'mapbox.streets',
    		accessToken: 'your.mapbox.access.token'
		}).addTo(mymap);

    	// Initialize a map with options
    	// map = new google.maps.Map(document.getElementById('map'), mapOptions);

		// Re-center map after window resize
		// google.maps.event.addDomListener(window, 'resize', function()
		// {
		// 	setTimeout(function()
		// 	{
		// 		google.maps.event.trigger(map, "resize");
		// 		map.setCenter(myLatlng);
		// 	}, 1400);
		// });
	}

});