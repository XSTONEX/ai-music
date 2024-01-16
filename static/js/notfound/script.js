$(document).ready(function() {
    

    // www.bootstrapmb.com
    function swingText(){
       
        if(!$('.swing-text').hasClass('down')){
                                   
            $('.swing-text').animate({
                rotate:'65deg',
               left:190,
                        bottom: 90
            },2000,function(){
                $('.swing-text').toggleClass('down');
            });    
        }else{
                                   
            $('.swing-text').animate({
                rotate:'70deg',
               left:180,
                        bottom: 100
            },2000,function(){
                $('.swing-text').toggleClass('down');
            });    
                                   
        }
       
                        
        setTimeout(swingText, 2000);
    }
                   
    function swingSpaceship(){
       
        if(!$('.swing').hasClass('down')){
                                   
            $('.swing').animate({
                left:5,
                top: 160
            },1500,function(){
                $('.swing').toggleClass('down');
            });    
        }else{
                                   
            $('.swing').animate({
                   
                left:0,
                top: 150
            },1500,function(){
                $('.swing').toggleClass('down');
            });    
                                   
        }
       
                        
        setTimeout(swingSpaceship, 1500);
    }
    
    $('#spaceship').animate({
                   
        left:0,
        top: 150
    },2000,function(){
        swingSpaceship(); 
        setTimeout(function(){
            $('#light').fadeIn(2000,function(){
                
                $('.err-text').animate({
                    rotate:'70deg',
                        left:180,
                        bottom: 100
                    },5000,function(){
                        swingText(); 
        
                    });
            });
            
            
        },1000);
    });    
                
                
      
                   
    $('#clouds').pan({
        fps: 25, 
        speed: 0.8, 
        dir: 'left', 
        depth: 300
    });
    $('#stars').pan({
        fps: 25, 
        speed: 0.2, 
        dir: 'left', 
        depth: 400
    });          
                   
                                

                      
  
    $('#mountain1').plaxify({
        "xRange":3,
        "yRange":0
    }) ;
    $.plax.enable();            
       
    $('#mountain2').plaxify({
        "xRange":-3,
        "yRange":0
    }) ;
        
    $('#mountain3').plaxify({
        "xRange":4,
        "yRange":0
    }) ;
                                        
                              
        
                            
                

                            
       
                                  
                                  

                                         
                                        
                                        
	$('#middle-content').height($(window).height());				
          
        
      
 
 

})
