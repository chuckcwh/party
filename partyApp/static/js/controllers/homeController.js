function homeController($scope) {


    $scope.myInterval = 5000;
    var slides = $scope.slides = [];
    $scope.addSlide = function() {
        var newWidth = slides.length + 1;
        slides.push({
            image: 'party' + newWidth + '.jpg',
            text: ['Heavy','Family','Lots of','Super'][slides.length % 4] + ' ' +
                ['Waves', 'Times', 'Funs', 'Awesome'][slides.length % 4]
        });
    };
    for (var i=0; i<4; i++) {
        $scope.addSlide();
    }

}