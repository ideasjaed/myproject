(function( $, undefined ) {

	$.Slideshow 				= function( options, element ) {
		this.$el	= $( element );
		this._init( options );
	};
	
	$.Slideshow.defaults 		= {
		jmpressOpts	: {
			viewPort 		: {
				height	: 350,
				width	: 10000,
				maxScale: 1
			},
			fullscreen		: false, 
			hash			: { use : false },
			mouse			: { clickSelects : false },
			keyboard		: { use : false },
			animation		: { transitionDuration : '1s' 
		}
		},
		arrows		: true,
		dots		: true,
		bgColorSpeed: '1s',
		autoplay	: false,
		interval	: 5000
    };
	
	$.Slideshow.prototype 	= {
		_init 				: function( options ) {
			
			this.options 		= $.extend( true, {}, $.Slideshow.defaults, options );
			this.$slides		= $('#Marco').children('div');
			this.slidesCount	= this.$slides.length;
			this.colors			= $.map( this.$slides, function( el, i ) { return $( el ).data( 'color' ); } ).join( ' ' );
			this._layout();
			this._initImpress();
			if( this.support ) {
				this._loadEvents();
				if( this.options.autoplay ) {
					this._startSlideshow();
				}				
			}			
		},
		_layout				: function() {
			
			this.$slides.each( function( i ) {
			
				$(this).addClass( 'step' + ( i + 1 ) );
			
			} );
			
			this.$jmsWrapper	= this.$slides.wrapAll( '<div class="wrapper"/>' ).parent();
			
			this.$jmsWrapper.css( {
				'-webkit-transition-duration' 	: this.options.bgColorSpeed,
				'-moz-transition-duration' 		: this.options.bgColorSpeed,
				'-ms-transition-duration' 		: this.options.bgColorSpeed,
				'-o-transition-duration' 		: this.options.bgColorSpeed,
				'transition-duration' 			: this.options.bgColorSpeed
			} );
			
		if( this.options.arrows ) {
			
				this.$arrows	= $( '<nav class="arrows"></nav>' );
				
				if( this.slidesCount > 1 ) {
				
					this.$arrowPrev	= $( '<span class="arrows-prev"/>' ).appendTo( this.$arrows );
					this.$arrowNext	= $( '<span class="arrows-next"/>' ).appendTo( this.$arrows );
					
				}

				this.$el.append( this.$arrows )
			
			}
			
			if( this.options.dots ) {			
				this.$dots		= $( '<nav class="dots"></nav>' );
				for( var i = this.slidesCount + 1; --i; ) {
					this.$dots.append( ( i === this.slidesCount ) ? '<span class="dots-current"/>' : '<span/>' );
				}
				
				if( this.options.jmpressOpts.start ) {
					
					this.$start		= this.$jmsWrapper.find( this.options.jmpressOpts.start ), idxSelected = 0;
					
					( this.$start.length ) ? idxSelected = this.$start.index() : this.options.jmpressOpts.start = null;
					
					this.$dots.children().removeClass( 'dots-current' ).eq( idxSelected ).addClass( 'dots-current' );
				
				}
				
				this.$el.append( this.$dots )
			
			}
			
		},
		_initImpress		: function() {
			
			var _self = this;
			
			this.$jmsWrapper.jmpress( this.options.jmpressOpts );
			this.support	= !this.$jmsWrapper.hasClass( 'not-supported' );
			
		if( !this.support ) {
			
				if( this.$arrows ) {
					this.$arrows.remove();				
				}
				
				if( this.$dots ) {
				
					this.$dots.remove();
				
				}
				
				return false;
			
			}
			
			this.$jmsWrapper.jmpress( 'setActive', function( slide, eventData ) {
				
				if( _self.options.dots ) {
					
					_self.$dots
						 .children()
						 .removeClass( 'dots-current' )
						 .eq( slide.index() )
						 .addClass( 'dots-current' );
				
				}
				
				this.removeClass( _self.colors );
				this.addClass( slide.data( 'color' ) );
				
			} );
			
			this.$jmsWrapper.addClass( this.$jmsWrapper.jmpress('active').data( 'color' ) );
			
		},
		_startSlideshow		: function() {		
			var _self	= this;			
			this.slideshow	= setTimeout( function() {
				
				_self.$jmsWrapper.jmpress( 'next' );
				
				if( _self.options.autoplay ) {
				
					_self._startSlideshow();
				
				}
			
			}, this.options.interval );
		
		},
		// stops the slideshow
		_stopSlideshow		: function() {
		
			if( this.options.autoplay ) {
					
				clearTimeout( this.slideshow );
				this.options.autoplay	= false;
			
			}
		
		},
		_loadEvents			: function() {
			
			var _self = this;
			
			// navigation arrows
			if( this.$arrowPrev && this.$arrowNext ) {
			
				this.$arrowPrev.on( 'click.jmslideshow', function( event ) {
					_self._stopSlideshow();
					_self.$jmsWrapper.jmpress( 'prev' );
					return false;
				} );
				this.$arrowNext.on( 'click.jmslideshow', function( event ) {
					_self._stopSlideshow();
					_self.$jmsWrapper.jmpress( 'next' );
					return false;
				
				} );
				
			}
			
			// navigation dots
			if( this.$dots ) {
			
				this.$dots.children().on( 'click.jmslideshow', function( event ) {
				 	
					_self._stopSlideshow();
					
					_self.$jmsWrapper.jmpress( 'goTo', '.step' + ( $(this).index() + 1 ) );
					
					return false;
				
				} );
			
			}
			
			this.$jmsWrapper.on( 'touchend.jmslideshow', function() {
F

			_self._stopSlideshow();
			
			} );
			
		}
	};
	
	var logError 			= function( message ) {
		if ( this.console ) {
			console.error( message );
		}
	};
	
	$.fn.jmslideshow		= function( options ) {
	
		if ( typeof options === 'string' ) {
			
			var args = Array.prototype.slice.call( arguments, 1 );
			
			this.each(function() {
			
				var instance = $.data( this, 'jmslideshow' );
				
				if ( !instance ) {
					logError( "cannot call methods on jmslideshow prior to initialization; " +
					"attempted to call method '" + options + "'" );
					return;
				}
				
				if ( !$.isFunction( instance[options] ) || options.charAt(0) === "_" ) {
					logError( "no such method '" + options + "' for jmslideshow instance" );
					return;
				}
				
				instance[ options ].apply( instance, args );
			
			});
		
		} 
		else {
		
			this.each(function() {
			
				var instance = $.data( this, 'jmslideshow' );
				if ( !instance ) {
					$.data( this, 'jmslideshow', new $.Slideshow( options, this ) );
				}
			});
		
		}
		return this;	
	};
})( jQuery );