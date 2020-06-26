/**
 * @license Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	config.protectedSource.push(/<(script)[^>]*>.*<\/script>/ig);
	config.protectedSource.push(/<(svg)[^>]*>.*<\/svg>/ig);
	config.contentsCss = ['/lib/DAN/DAN.css', '/plugins/ckeditor/contents.css'];
};
