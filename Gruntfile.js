module.exports = function (grunt) {
    grunt.initConfig({
        uglify: {
            compilar: {
                expand: true,
                cwd: 'core/assets/js',
                src: '**/*.js',
                dest: 'core/static/js'
            }
        },
        sass: {
            compilar: {
                expand: true,
                cwd: 'core/assets/scss',
                src: ['*.scss'],
                dest: 'core/static/css',
                ext: '.css'
            },
            options: {
                style: 'compressed'
            }
        },
        imagemin: {
            dynamic: {                         // Another target
                files: [{
                    expand: true,
                    cwd: 'core/assets/images/',                   // Src matches are relative to this path
                    src: ['*.{png,jpg,gif}'],   // Actual patterns to match
                    dest: 'core/static/images/'                  // Destination path prefix
                }]
            }
        },
        jshint: {
            files: {
                src: 'core/assets/js/*.js'
            }
        },
        watch:{
            sass: {
                files: 'core/assets/scss/*.scss',
                tasks: 'sass:compilar'
            },
            uglify: {
                files: 'core/assets/js/*.js',
                tasks: 'uglify:compilar'
            },
            img: {
                files: 'core/assets/images/*.*',
                tasks: 'imagemin'
            },
            jshint: {
                files: 'core/assets/js/*.js',
                tasks: 'jshint'
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-watch');

};