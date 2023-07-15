var fullScreenRenderer = vtk.Rendering.Misc.vtkFullScreenRenderWindow.newInstance({
    container: document.querySelector('#cone_container'),
    background: [1., 1., 1.]
});

var actor = vtk.Rendering.Core.vtkActor.newInstance();
var mapper = vtk.Rendering.Core.vtkMapper.newInstance();
var cone = vtk.Filters.Sources.vtkConeSource.newInstance();

actor.setMapper(mapper);
mapper.setInputConnection(cone.getOutputPort());

var renderer = fullScreenRenderer.getRenderer();
renderer.addActor(actor);
renderer.resetCamera();

var renderWindow = fullScreenRenderer.getRenderWindow();
renderWindow.render();

var slider = document.querySelector('#cone_slider');
slider.addEventListener('input', function (e) {
  var resolution = Number(e.target.value);
  cone.setResolution(resolution);
  renderWindow.render();
});
