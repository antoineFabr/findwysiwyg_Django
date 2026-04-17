tinymce.PluginManager.add('custom_plugin', function(editor, url) {

    editor.ui.registry.addButton('custom_button', {
        text: 'custom button',
        tooltip: 'Cutom composant',
        onAction: function () {
            editor.insertContent(
                '<div style="background:#eee; padding:10px; border-left:4px solid #0056b3;">' +
                '<strong>Contenu généré par mon plugin custom !</strong>' +
                '</div><p>&nbsp;</p>'
            );
        }
    });
});
