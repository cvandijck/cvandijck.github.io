//Select div for rendering
const vtkRenderScreen = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance({
    container: document.querySelector('#cone'),
    background: [1., 1., 1.]
});

vtkRenderScreen.R = [0., 0., 0.]

//Create volume to render
const actor = vtk.Rendering.Core.vtkActor.newInstance();
const mapper = vtk.Rendering.Core.vtkMapper.newInstance();
const cone = vtk.Filters.Sources.vtkConeSource.newInstance();


// create orientation widget
const axes = vtk.Rendering.Core.vtkAxesActor.newInstance();
const orientationWidget = vtk.Interaction.Widgets.vtkOrientationMarkerWidget.newInstance({
    actor: axes,
    interactor: vtkRenderScreen.getRenderWindow().getInteractor(),
});
orientationWidget.setEnabled(true);
orientationWidget.setViewportCorner(
    vtk.Interaction.Widgets.vtkOrientationMarkerWidget.Corners.BOTTOM_RIGHT
);
orientationWidget.setViewportSize(0.15);
orientationWidget.setMinPixelSize(100);
orientationWidget.setMaxPixelSize(300);

actor.setMapper(mapper);
mapper.setInputConnection(cone.getOutputPort());
vtkRenderScreen.getRenderer().addActor(actor);
vtkRenderScreen.getRenderer().resetCamera();

//Start rendering
vtkRenderScreen.getRenderWindow().render();