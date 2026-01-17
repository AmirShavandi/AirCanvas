import cv2
import numpy as np

cap = cv2.VideoCapture(0)

tracker = None
bbox = None
tracking = False

canvas = None
prev_center = None

trail_color = (255, 255, 255)  # white trail on canvas
trail_thickness = 6

while True:
    ok, frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    if tracking and bbox is not None:
        ok, bbox = tracker.update(frame)

        if ok:
            x, y, bw, bh = [int(v) for v in bbox]

            # Green tracking rectangle
            cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
            cv2.putText(frame, "Tracking", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Center of the box
            cx = x + bw // 2
            cy = y + bh // 2
            center = (cx, cy)

            # Draw movement trail on separate canvas
            if prev_center is not None:
                cv2.line(canvas, prev_center, center, trail_color, trail_thickness)

            prev_center = center

        else:
            cv2.putText(frame, "Lost (press r)", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            prev_center = None

    cv2.putText(frame, "r=select | c=clear canvas | q=quit", (10, h - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Tracker", frame)
    cv2.imshow("Draw Screen", canvas)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    if key == ord("c"):
        canvas[:] = 0
        prev_center = None

    if key == ord("r"):
        bbox = cv2.selectROI("Tracker", frame, fromCenter=False, showCrosshair=True)
        tracker = cv2.legacy.TrackerMOSSE_create()
        tracker.init(frame, bbox)
        tracking = True
        prev_center = None

cap.release()
cv2.destroyAllWindows()