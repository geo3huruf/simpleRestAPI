f r o m   a p p   i m p o r t   a p p ,   s c r a p 
 f r o m   f l a s k   i m p o r t   r e n d e r _ t e m p l a t e ,   s e n d _ f i l e   , f l a s h ,   u r l _ f o r 
 f r o m   f l a s k   i m p o r t   r e q u e s t 
 f r o m   a p p . f o r m s   i m p o r t   L o g i n F o r m 
 i m p o r t   r e q u e s t s ,   j s o n ,   r a n d o m 
 
 @ a p p . r o u t e ( ' / ' ) 
 @ a p p . r o u t e ( ' / i n d e x ' ) 
 d e f   h o m e ( ) : 
 	 r e t u r n   r e n d e r _ t e m p l a t e ( ' i n d e x . h t m l ' , t i t l e = ' L E S S O N ' ) 
 
 @ a p p . r o u t e ( ' / i m a g e ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ i m a g e ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' q u e r y ' ] 
 	 t h i s _ r e s t   =   s c r a p . i m g ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 # j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
@ a p p . r o u t e ( ' api/ yt_search' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ yt_search( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' q u e r y ' ] 
 	 t h i s _ r e s t   =   s c r a p . yt_search( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / k o d e p o s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ k o d e P o s t ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' k o t a ' ] 
 	 t h i s _ r e s t   =   s c r a p . k o d e P o s t ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / s h o l a t ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ A d z a n ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' k o t a ' ] 
 	 t h i s _ q u e r y 1   =   r e q u e s t . a r g s [ ' t h ' ] 
 	 t h i s _ q u e r y 2   =   r e q u e s t . a r g s [ ' b l n ' ] 
 	 t h i s _ q u e r y 3   =   r e q u e s t . a r g s [ ' t g l ' ] 
 	 t h i s _ r e s t   =   s c r a p . A d z a n ( t h i s _ q u e r y ,   t h i s _ q u e r y 1 ,   t h i s _ q u e r y 2 ,   t h i s _ q u e r y 3 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / q u r a n l i s t ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ Q u r a n l i s t ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' r e s u l t ' ] 
 	 t h i s _ r e s t   =   s c r a p . Q u r a n l i s t ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / q u r a n ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ Q u r a n ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' n u m b e r ' ] 
 	 t h i s _ r e s t   =   s c r a p . Q u r a n ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / n e w s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ n e w s S i n d o ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' s e a r c h ' ] 
 	 t h i s _ r e s t   =   s c r a p . n e w s S i n d o ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / s i m i ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d S i m i s i m i ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d S i m i s i m i ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / s t a f a ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s t a f a ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' s e a r c h ' ] 
 	 t h i s _ r e s t   =   s c r a p . s t a f a ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / d l m p 3 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ d l S t f a ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' c o d e ' ] 
 	 t h i s _ r e s t   =   s c r a p . d l S t f a ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / k o m i k _ a p i ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ k o m i k ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' i d ' ] 
 	 t h i s _ r e s t   =   s c r a p . k o m i k ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / k o m i k _ l i s t / a p i ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ k o m i k L i s t ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . k o m i k L i s t ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / k o m i k _ r e s / a p i ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ k o m i k R e s ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . k o m i k R e s ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 	 
 @ a p p . r o u t e ( ' / k o m i k _ s e a r c h / a p i ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ k o m i k S e a r c h ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' s e a r c h ' ] 
 	 t h i s _ r e s t   =   s c r a p . k o m i k S e a r c h ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / g o o g l e s e a r c h ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ g o S e a r c h ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' q u e r y ' ] 
 	 t h i s _ r e s t   =   s c r a p . g o S e a r c h ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / x v i d e o s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ V i d e o X ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' s e a r c h ' ] 
 	 t h i s _ q u e r y 1   =   r e q u e s t . a r g s [ ' p a g e ' ] 
 	 t h i s _ r e s t   =   s c r a p . V i d e o X ( t h i s _ q u e r y , t h i s _ q u e r y 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / x d o w n l o a d ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ V i d e o D L ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . V i d e o D L ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i / s t a r m a c k e r ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s t a r M a k e r ( ) : 
         t h i s _ q u e r y   =   r e q u e s t s . a r g s [ " u r l " ] 
         t h i s _ r e s t   =   s c r a p . s t a r M a k e r ( t h i s _ q u e r y ) 
         r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
         
 @ a p p . r o u t e ( ' / r a n d o m i m g ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ r a n d o m i m g ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' q u e r y ' ] 
 	 t h i s _ r e s t   =   s c r a p . r a n d o m i m g ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i _ t i n y ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ a p i t i n y ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . a p i t i n y ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i _ c u a c a ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ T z o n e ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' k o t a ' ] 
 	 t h i s _ r e s t   =   s c r a p . T z o n e ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 # = = = = = = = = = = = [   Z M e d i a   ] = = = = = = = = = = = = = = = = 
 @ a p p . r o u t e ( ' / a r t i n a m e ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ a r t i N a m e ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' q u e r y ' ] 
 	 t h i s _ r e s t   =   s c r a p . a r t i N a m e ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / i n s t a d l ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d I g r a m ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d I g r a m ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / s m u l e ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s m u l i d ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' i d ' ] 
 	 t h i s _ r e s t   =   s c r a p . s m u l i d ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / i n f o g e m p a ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ i n g e m p a ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a g e ' ] 
 	 t h i s _ r e s t   =   s c r a p . i n g e m p a ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 
 @ a p p . r o u t e ( ' / a p i / s m u l e d l ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d S m u l e ( ) : 
         t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' u r l ' ] 
         t h i s _ r e s t   =   s c r a p . s e n d S m u l e ( t h i s _ q u e r y ) 
         r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
         
 @ a p p . r o u t e ( ' / a p i / s m u l e d l 1 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s m u l e ( ) : 
         t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' u r l ' ] 
         t h i s _ r e s t   =   s c r a p . s m u l e ( t h i s _ q u e r y ) 
         r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
         
 @ a p p . r o u t e ( ' / a p i / z o d i a k ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ z o d i a k ( ) : 
         t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' z o d i a k ' ] 
         t h i s _ r e s t   =   s c r a p . z o d i a k ( t h i s _ q u e r y ) 
         r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 	 
 # = = = = # = = # # = # = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
 @ a p p . r o u t e ( ' / t e x t a v a t a r ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ t e x t V i d e o ( ) : 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' q u e r y ' ] 
 	 t h i s _ r e s t   =   s c r a p . t e x t V i d e o ( t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 
 @ a p p . r o u t e ( ' / a p i / n u m b e r p l a t e ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ n u m b e r _ p l a t e ( ) : 
         t h i s _ t e x t   =   r e q u e s t . a r g s [ ' t e x t ' ] 
         t h i s _ t e x t 1   =   r e q u e s t . a r g s [ ' c o l o r ' ] 
         t h i s _ r e s t   =   s c r a p . n u m b e r _ p l a t e ( t h i s _ t e x t ,   t h i s _ t e x t 1 ) 
         r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
         
 @ a p p . r o u t e ( ' / p h o t o f u n / v a l e n t i n e s _ d a y ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d V a l d a y ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d V a l d a y ( t h i s _ p a t h ,   t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / s u m m e r - d i a r y ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d S u m m e r ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ p a t h 1   =   r e q u e s t . a r g s [ ' p a t h 1 ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d S u m m e r ( t h i s _ p a t h ,   t h i s _ p a t h 1 ,   t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / f l o w e r s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d C l o w e r s ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d C l o w e r s ( t h i s _ p a t h ,   t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / m e m o r i e s _ o f _ p a r i s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P a r i s ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P a r i s ( t h i s _ p a t h ,   t h i s _ q u e r y ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / v e r y - o l d - b o o k ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d b o o k ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ q u e r y 1   =   r e q u e s t . a r g s [ ' t e x t 1 ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d b o o k ( t h i s _ p a t h ,   t h i s _ q u e r y ,   t h i s _ q u e r y 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / o p e n - b o o k ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d o p e n ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ q u e r y 1   =   r e q u e s t . a r g s [ ' t e x t 1 ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d o p e n ( t h i s _ p a t h ,   t h i s _ q u e r y ,   t h i s _ q u e r y 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / d a i l y - n e w s p a p e r ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d d a i l y ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ q u e r y 1   =   r e q u e s t . a r g s [ ' t e x t 1 ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d d a i l y ( t h i s _ p a t h ,   t h i s _ q u e r y ,   t h i s _ q u e r y 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / m o r n i n g _ n e w s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d m o r n i n g ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ q u e r y   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ q u e r y 1   =   r e q u e s t . a r g s [ ' t e x t 1 ' ] 
 	 t h i s _ q u e r y 2   =   r e q u e s t . a r g s [ ' t e x t 2 ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d m o r n i n g ( t h i s _ p a t h ,   t h i s _ q u e r y ,   t h i s _ q u e r y 1 ,   t h i s _ q u e r y 2 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / p h o t o f u n / b a c k _ c o v e r ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d c o v e r ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d c o v e r ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / l e g e n d s / a v a t a r ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 2 8 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 2 8 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / l e g e n d s / w i n g s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 4 3 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 4 3 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / l e g e n d s / c h a m p i o n s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d C h a m p ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d C h a m p ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i _ a v a t a r ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 2 3 1 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ p a t h 1   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 2 3 1 ( t h i s _ p a t h ,   t h i s _ p a t h 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i _ m a s t e r y ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 8 1 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ p a t h 1   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 8 1 ( t h i s _ p a t h ,   t h i s _ p a t h 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i _ b e a u t i f u l ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 3 8 4 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 3 8 4 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i / l o g o 1 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d L o g o ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d L o g o ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / l o g o 2 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 1 8 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 1 8 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / l o g o 3 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 1 6 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 1 6 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / l o g o 4 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 7 4 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 7 4 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / l o g o 5 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 7 0 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 7 0 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / l o g o 6 ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 7 1 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 7 1 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i _ b a c k g r o u n d ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 3 4 9 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 3 4 9 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i _ c o v e r f b ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 3 0 1 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ p a t h 1   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 3 0 1 ( t h i s _ p a t h ,   t h i s _ p a t h 1 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i _ b u r n e d ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 9 3 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 9 3 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i _ p e n s i l ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 2 2 6 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 2 2 6 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	 
 @ a p p . r o u t e ( ' / a p i / m o c k u p ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 3 9 8 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 3 9 8 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 @ a p p . r o u t e ( ' / a p i / p o k e m o n ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d P h o t o x y _ 1 4 8 ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' u r l ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d P h o t o x y _ 1 4 8 ( t h i s _ p a t h ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ) 
 	 
 # = = = = = = = = = = = [ F O T O F U N I A ] = = = = = = = = = = = = 
 @ a p p . r o u t e ( ' / p h o t o f u n / b r e a k i n g - n e w s ' , m e t h o d s = [ ' P O S T ' , ' G E T ' ] ) 
 d e f   r e s t _ s e n d N e w s ( ) : 
 	 t h i s _ p a t h   =   r e q u e s t . a r g s [ ' p a t h ' ] 
 	 t h i s _ t e x t   =   r e q u e s t . a r g s [ ' t e x t ' ] 
 	 t h i s _ t e x t 2   =   r e q u e s t . a r g s [ ' t e x t 2 ' ] 
 	 t h i s _ t e x t 3   =   r e q u e s t . a r g s [ ' t e x t 3 ' ] 
 	 t h i s _ r e s t   =   s c r a p . s e n d N e w s ( t h i s _ p a t h ,   t h i s _ t e x t ,   t h i s _ t e x t 2 ,   t h i s _ t e x t 3 ) 
 	 r e t u r n   j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ,   s o r t _ k e y s = T r u e ) 
 	   # j s o n . d u m p s ( t h i s _ r e s t ,   i n d e n t = 4 ) 
 	   
 	   
 # l i n e   =   N e w Q R L o g i n ( ) 
 # t o k e n ,   c e r t   =   l i n e . l o g i n W i t h Q r C o d e ( " a n d r o i d _ l i t e " ) 
 # p r i n t   ( " A c c e s s   T o k e n :   "   +   t o k e n ) 
 # p r i n t   ( " C e r t i f i c a t e :   "   +   c e r t ) 
 