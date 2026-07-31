def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    Assumes format: [x_min, y_min, x_max, y_max]
    """
    x1, y1, x2, y2 = box_a
    x3, y3, x4, y4 = box_b
    area_a = (x2 - x1) * (y2 - y1)
    area_b = (x4 - x3) * (y4 - y3)
    
    ix1 = max(x1, x3)
    iy1 = max(y1, y3)
    ix2 = min(x2, x4)
    iy2 = min(y2, y4) 
    
    inter_width = max(0, ix2 - ix1)
    inter_height = max(0, iy2 - iy1)
    area_intersection = inter_width * inter_height
    
    area_union = area_a + area_b - area_intersection
    
    if area_union == 0:
        return 0.0
        
    return area_intersection / area_union