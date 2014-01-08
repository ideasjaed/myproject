

$(window).scroll(function()
		{
			if ($(this).scrollTop() > 50) $('nav').addClass("fixed").fadeIn();
			else $('nav').removeClass("fixed");
		});