from src import CalibrationRectification 

recticlass = CalibrationRectification.CalibrationRectification()
recticlass.calibrate()
recticlass.remap_from_path("sample/")
