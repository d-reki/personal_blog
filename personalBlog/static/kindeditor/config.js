KindEditor.ready(function(K) {
    window.editor = K.create('#id_content',{
        resizeType : 1,
        themeType : 'simple',
        width : '100%',
        height : '400px',
        // uploadJson : 'media/',
        allowPreviewEmoticons : false,
        allowImageRemote : false,
        uploadJson : '/account/upload/kindeditor',
    });
    
});